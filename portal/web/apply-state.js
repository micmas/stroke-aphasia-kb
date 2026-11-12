// Presentation only: counts come from the workflow, never from a timer or inbox deltas.
export function applyState(run) {
  if (!run) return { label: '', busy: false, poll: false, next: '' };
  if (run.status !== 'completed') {
    const p = run.progress;
    const phase = p?.phase === 'published' ? 'publishing' : run.phase || p?.phase;
    const labels = { applying: 'Applying records…', registering: 'Registering papers…', checking: 'Checking changes…',
      publishing: 'Publishing changes…', preparing: 'Preparing to apply…' };
    const label = phase === 'applying' && p?.total > 0 && p.current > 0
      ? `Applying ${p.current} of ${p.total}` : labels[phase] || 'Preparing to apply…';
    return { label, busy: true, poll: true,
      next: 'No local action needed while this runs. Changes are checked before publication.' };
  }
  if (run.conclusion !== 'success') return { label: 'Apply needs attention', busy: false, poll: false,
    next: 'Open the run to see the problem. Do not assume the changes were published.' };
  if (run.publication?.status === 'failure') return { label: 'Site rebuild needs attention', busy: false, poll: false,
    next: 'The records were applied, but a site rebuild failed. Open the rebuild run for details.' };
  if (run.publication?.status === 'in_progress') return { label: 'Rebuilding sites…', busy: true, poll: true,
    next: 'Your records are applied. Wait for the sites to finish rebuilding; no terminal command is needed.' };
  return { label: 'Apply complete', busy: false, poll: false,
    next: run.publication?.status === 'success'
      ? 'Both sites are updated. Refresh this page and continue screening. No local action is needed for screening decisions.'
      : 'Apply succeeded. Allow the sites to rebuild, then refresh this page. No local action is needed for screening decisions.' };
}
