# Defensive response playbook

## Detection
- Monitor relevant local events, suspicious process behavior, file-integrity changes and authentication anomalies.
- Correlate alerts to reduce noise and verify before disruption.

## Assessment
- Distinguish false positives from incidents.
- Establish affected scope, business impact and available evidence.

## Containment
- Isolate or restrict only owned and authorized resources.
- Preserve evidence and log each change.
- Require operator approval for destructive or high-availability impact actions.

## Recovery
- Verify clean restoration points and unchanged protected files.
- Reenable services in stages and monitor regressions.

## Learning
- Feed validated incident outcomes back into alert rules and evaluation datasets.
- Review model drift and changes through controlled testing.

**Limits:** No hack-back, unauthorized testing, or promise of perfect protection. Human accountability remains central to high-impact response.
