# cloudops-inspector

[![CI](https://github.com/ptlriya0013-cloud/cloudops-inspector/actions/workflows/ci.yml/badge.svg)](https://github.com/ptlriya0013-cloud/cloudops-inspector/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)

A lightweight CLI tool for inspecting disk usage and scanning log files for errors — built to demonstrate a complete, real-world DevOps engineering workflow (issue tracking, branching, code review, CI/CD, and releases).

## Status
✅ Core CLI, CI pipeline, branch protection, and contribution workflow in place. Actively adding features — see the [project board](../../projects) and [open issues](../../issues).

## Features
- Disk usage inspection with configurable threshold alerts
- Log file scanning for ERROR/WARNING patterns
- `--json` output on both commands, for CI/scripting use

## Installation

```bash
git clone https://github.com/ptlriya0013-cloud/cloudops-inspector.git
cd cloudops-inspector
pip install -r requirements-dev.txt
```

## Usage

**Check disk usage:**
```bash
python -m cloudops_inspector.cli disk
# Mount: C:\
# Total: 455.61 GB | Used: 396.43 GB (87.0%)
# WARNING: usage exceeds 80.0% threshold!
```

**Check disk usage with a custom threshold, as JSON:**
```bash
python -m cloudops_inspector.cli disk --threshold 90 --json
# {"mount": "C:\\", "total_gb": 455.61, "used_gb": 396.43, "percent_used": 87.0, "threshold_exceeded": false}
```

**Scan a log file:**
```bash
python -m cloudops_inspector.cli logs /path/to/app.log
# Errors: 2 | Warnings: 1
#
# Last errors:
#   ERROR: connection timeout
```

## Development

```bash
pip install -r requirements-dev.txt
pytest -v
flake8 cloudops_inspector --max-line-length=100
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow: issue → branch → PR → review → CI → merge.

## Security

See [SECURITY.md](SECURITY.md) for how to report vulnerabilities.

## License

MIT — see [LICENSE](LICENSE)