#!/usr/bin/env python3
"""User-facing commands for the stroke aphasia knowledge base."""
from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parent
COMMANDS = {
    'prepare': ('prepare_dual_batch.py', [], 'Create a frozen paper manifest'),
    'extract': ('batch_dual_extract.py', [], 'Preview or run two independent local extractions'),
    'review': ('review_dual_extract.py', [], 'Preview or run local source reconciliation'),
    'status': ('kb_status.py', [], 'Inspect knowledge-base content and provenance'),
    'drafts': ('promote.py', ['--list'], 'List existing KB drafts awaiting approval'),
    'inspect': ('review_app.py', [], 'Open the local review workbench (edits are logged)'),
    'validate': ('aphasia_kb.py', [], 'Check or query the knowledge base'),
}


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ['--help', '-h', 'help']:
        if len(argv) == 2 and argv[0] == 'help' and argv[1] in COMMANDS:
            argv = [argv[1], '--help']
        else:
            print('Usage: python kb.py COMMAND [options]\n')
            for heading, names in [('Provisional source pipeline', ['prepare', 'extract', 'review']), ('Existing KB drafts and data', ['drafts', 'inspect', 'validate']), ('Read-only overview', ['status'])]:
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
    if command == 'status' and '--tag-legacy' in args:
        print('status is read-only in this interface; historical provenance is preserved without retagging.', file=sys.stderr)
        return 2
    if command == 'drafts' and any(a not in ['--help', '-h'] for a in args):
        print('drafts lists pending KB drafts. See docs/GOVERNANCE.md for approval.', file=sys.stderr)
        return 2
    script, fixed, _ = COMMANDS[command]
    if command == 'prepare' and not any(a == '--repo' or a.startswith('--repo=') for a in args):
        fixed = ['--repo', str(ROOT)]
    # Replace the wrapper process: interrupts and exit status belong to the real job.
    # No shell interpretation, new inference logic, or changes to the existing runners.
    os.execv(sys.executable, [sys.executable, str(ROOT/'scripts'/script), *fixed, *args])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
