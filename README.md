# SLO / Error Budget Toolkit

Practical SRE toolkit for defining SLOs, calculating error budgets, and alerting on burn rate.

## Contents

- Example SLI/SLO definitions (availability + latency)
- Multi-window multi-burn-rate Prometheus rules
- Simple Python error budget calculator
- Template for service level objectives document

## Quick example

```bash
python scripts/error_budget.py --slo 99.9 --window 30d --error-rate 0.002
```

Created for SRE/DevOps portfolio – https://github.com/hkotaga-source
