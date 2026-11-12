#!/usr/bin/env python3
"""User-facing commands for the stroke aphasia knowledge base."""
from pathlib import Path
import os
import sys
import subprocess
import time
import fcntl
import json
import shlex

ROOT = Path(__file__).resolve().parent
COMMANDS = {
    'sync': (None, [], 'Download portal PDFs and publish receipts; never run models'),
    'intake': ('intake_papers.py', [], 'Prepare downloaded PDFs; no model extraction'),
    'prepare': ('prepare_dual_batch.py', [], 'Create a frozen paper manifest'),
    'extract': ('batch_dual_extract.py', [], 'Preview or run two independent local extractions'),
    'review': ('review_dual_extract.py', [], 'Preview or run local source reconciliation'),
    'status': ('kb_status.py', [], 'Inspect knowledge-base content and provenance'),
    'drafts': ('promote.py', ['--list'], 'List existing KB drafts awaiting approval'),
    'inspect': ('review_app.py', [], 'Open the local review workbench (edits are logged)'),
    'validate': ('aphasia_kb.py', [], 'Check or query the knowledge base'),
}



def git(*args, capture=True):
    return subprocess.run(['git', *args], cwd=ROOT, check=True, text=True,
                          stdout=subprocess.PIPE if capture else None).stdout


def active_jobs():
    """Include older script launches that predate the shared command lock."""
    result = subprocess.run(['ps', '-axo', 'pid=,command='], check=True,
                            capture_output=True, text=True)
    runners = ('batch_dual_extract.py', 'dual_extract.py', 'review_dual_extract.py',
               'extract_analysis_inventory.py', 'batch_extract.py', 'auto_review.py',
               'extract.py', 'recheck_drafts.py', 'refocus.py', 'intake_papers.py')
    jobs = []
    for line in result.stdout.splitlines():
        fields = line.strip().split(None, 1)
        if len(fields) != 2 or int(fields[0]) == os.getpid():
            continue
        command = fields[1]
        try:
            tokens = shlex.split(command)
        except ValueError:
            continue
        if (tokens and Path(tokens[0]).name.lower().startswith('python')
                and any(Path(token).name in runners for token in tokens[1:])):
            jobs.append(line.strip())
    return jobs


def model_command(command, args, invocation, operation=None):
    wait = '--wait' in args
    # argparse accepts abbreviated flags; guard those too before delegation.
    if not any(a in ('--run', '--ru', '--r') for a in args):
        if wait:
            print('--wait requires --execute.' if command == 'intake' else '--wait requires --run.', file=sys.stderr)
            return 2
        os.execv(sys.executable, invocation)
        return 0
    lock_path = Path(git('rev-parse', '--git-common-dir').strip())
    if not lock_path.is_absolute():
        lock_path = ROOT / lock_path
    with (lock_path / 'kb-model.lock').open('a') as lock:
        announced = False
        while True:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                busy = active_jobs()
                if not busy:
                    break
                fcntl.flock(lock, fcntl.LOCK_UN)
            except BlockingIOError:
                busy = ['Another KB processing command is running.']
            if not wait:
                print('KB processing is busy. No work started. Use --wait to wait, or run later.\n' + '\n'.join(busy))
                return 2
            if not announced:
                print('Waiting for the existing KB processing job. Ctrl-C cancels this wait.', flush=True)
                announced = True
            time.sleep(5)
        if operation is not None:
            return operation()
        return run_child(invocation)


def run_child(invocation):
    # The caller retains its lock until its child finishes, including interruption.
    child = subprocess.Popen(invocation, cwd=ROOT)
    try:
        return child.wait()
    except KeyboardInterrupt:
        child.send_signal(2)
        child.wait()
        return 130


def intake_operation(invocation):
    common = Path(git('rev-parse', '--git-common-dir').strip())
    if not common.is_absolute():
        common = ROOT / common
    with (common / 'kb-sync.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('PDF sync is running. Intake has not started; try again after sync finishes.')
            return 2
        return run_child(invocation)


def sync(args, with_intake=False):
    if args in (['--help'], ['-h']):
        print('Usage: python kb.py sync [--intake [--wait]]\nDownload PDFs and publish receipts. --intake also prepares PDFs and syncs the portal.\nNo model extraction. --wait keeps this terminal waiting for a busy KB job.\nRequires main, no staged changes, and clean import records; --intake also requires clean bibliography and PDF index.')
        return 0
    if args:
        if '--intake' not in args or any(a not in ('--intake', '--wait') for a in args):
            print('Use sync [--intake [--wait]]; extraction is separate.', file=sys.stderr)
            return 2
        guard = ['--run'] + (['--wait'] if '--wait' in args else [])
        return model_command('intake', guard, [], operation=lambda: sync([], with_intake=True))
    paths = ['screening/candidates.yaml', 'logs/portal/inbox',
             'logs/portal/applied', 'logs/portal/ledger.jsonl', 'logs/extraction_log.md']
    if with_intake:
        paths += ['citations.md', 'portal/papers.json']
    common = Path(git('rev-parse', '--git-common-dir').strip())
    if not common.is_absolute():
        common = ROOT / common
    with (common / 'kb-sync.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('A PDF sync is already running.')
            return 2
        if git('branch', '--show-current').strip() != 'main':
            raise ValueError('Switch to main before syncing.')
        if git('diff', '--cached', '--name-only').strip():
            raise ValueError('There are staged changes. Commit or unstage them before syncing.')
        if git('status', '--porcelain', '--', *paths).strip():
            raise ValueError('Local import records have unpublished changes. Review and commit them before syncing; they have been preserved.')
        git('fetch', 'origin', 'main', capture=False)
        if active_jobs() and git('diff', 'HEAD', 'origin/main', '--', 'scripts', 'kb.py').strip():
            raise ValueError('An active model job is using older code. Sync after it finishes; its files were not changed.')
        git('merge', '--ff-only', 'origin/main', capture=False)
        # Each upload is checked independently, including retained pre-processing originals.
        # A conflicting replacement stays pending without blocking unrelated receipts.
        sys.path.insert(0, str(ROOT / 'scripts'))
        import portal_import as importer
        importer.run(True, False, 'pdf', intake=False)
        if with_intake:
            subprocess.run([sys.executable, str(ROOT / 'scripts/intake_papers.py'),
                            '--execute', '--no-sync'], cwd=ROOT, check=True)
            subprocess.run([sys.executable, str(ROOT / 'scripts/publish_portal.py'),
                            '--sync'], cwd=ROOT, check=True)
        files = git('ls-files', '-z', '--cached', '--others', '--exclude-standard', '--', *paths)
        files = list(dict.fromkeys(f for f in files.split('\0') if f))
        if files:
            git('add', '-A', '--', *files)
        if git('diff', '--cached', '--name-only').strip():
            git('commit', '-m', 'Sync and prepare portal PDFs' if with_intake else 'Sync portal PDF download receipts', capture=False)
        git('push', 'origin', 'main', capture=False)
        remaining = sum(json.loads(p.read_text()).get('kind') == 'pdf'
                        for p in importer.INBOX.glob('*.json'))
        print(f'Sync published. {remaining} PDF upload(s) remain. No models started.')
        return 1 if remaining else 0


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ['--help', '-h', 'help']:
        if len(argv) == 2 and argv[0] == 'help' and argv[1] in COMMANDS:
            argv = [argv[1], '--help']
        else:
            print('Usage: python kb.py COMMAND [options]\n')
            for heading, names in [('PDF download and preparation', ['sync', 'intake']), ('Provisional source pipeline', ['prepare', 'extract', 'review']), ('Existing KB drafts and data', ['drafts', 'inspect', 'validate']), ('Read-only overview', ['status'])]:
                print(heading + ':')
                for name in names:
                    print(f'  {name:10} {COMMANDS[name][2]}')
            print('\nUse COMMAND --help for options. Start with docs/HOWTO.md.\n'
                  'Prepare writes a manifest. Extract and review preview unless --run is supplied.\n'
                  'Model outputs are provisional; review outputs are not KB drafts.\n'
                  'Mapping is manual (docs/HOWTO.md); approval uses promote.py under docs/GOVERNANCE.md.')
            return 0
    command, args = argv[0], argv[1:]
    if command not in COMMANDS:
        print(f'Unknown command: {command}. Use python kb.py --help.', file=sys.stderr)
        return 2
    if command == 'sync':
        try:
            return sync(args)
        except (ValueError, subprocess.CalledProcessError) as error:
            print(f'Sync stopped: {error}. Local work is preserved.', file=sys.stderr)
            return 1
    if command == 'status' and args == ['--jobs']:
        jobs = active_jobs()
        print('\n'.join(jobs) if jobs else 'No active KB model processes found.')
        return 0
    if command == 'status' and '--tag-legacy' in args:
        print('status is read-only in this interface; historical provenance is preserved without retagging.', file=sys.stderr)
        return 2
    if command == 'drafts' and any(a not in ['--help', '-h'] for a in args):
        print('drafts lists pending KB drafts. See docs/GOVERNANCE.md for approval.', file=sys.stderr)
        return 2
    if command == 'intake':
        allowed = {'--execute', '--wait', '--from', '--papers-dir', '--no-ocr',
                   '--no-register', '--no-sync', '--allow-probable', '--help', '-h'}
        if any(a.startswith('-') and a.split('=', 1)[0] not in allowed for a in args):
            print('Use full intake options from kb.py intake --help. Extraction is separate.', file=sys.stderr)
            return 2
        if '--help' in args or '-h' in args:
            print('Usage: python kb.py intake [--execute] [--wait] [options]\n'
                  'Preview PDF preparation; --execute applies it. No model extraction.\n'
                  'Options: --from DIR, --papers-dir DIR, --no-ocr, --no-register,\n'
                  '         --no-sync, --allow-probable. --wait requires --execute.\n'
                  'For download, intake and publishing together use kb.py sync --intake.')
            return 0
    script, fixed, _ = COMMANDS[command]
    if command == 'prepare' and not any(a == '--repo' or a.startswith('--repo=') for a in args):
        fixed = ['--repo', str(ROOT)]
    # Replace the wrapper process: interrupts and exit status belong to the real job.
    # No shell interpretation, new inference logic, or changes to the existing runners.
    invocation = [sys.executable, str(ROOT/'scripts'/script), *fixed, *[a for a in args if a != '--wait']]
    if command == 'intake':
        guard = (['--run'] if '--execute' in args else []) + (['--wait'] if '--wait' in args else [])
        return model_command(command, guard, invocation, operation=lambda: intake_operation(invocation))
    if command in ('extract', 'review'):
        return model_command(command, args, invocation)
    os.execv(sys.executable, invocation)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
