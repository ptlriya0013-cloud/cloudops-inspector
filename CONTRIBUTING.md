# Contributing to cloudops-inspector

Thanks for your interest in contributing! This document outlines the workflow used in this repository.

## Workflow

1. **Open an issue** describing the bug or feature before starting work.
2. **Create a branch** from `main`, named `feature/<issue-number>-short-description` or `fix/<issue-number>-short-description`.
3. **Make your changes**, following the code style below.
4. **Write or update tests** for any behavior change.
5. **Commit using Conventional Commits** (see below).
6. **Open a pull request** against `main`, referencing the issue (`Closes #<number>`).
7. **Wait for CI to pass** and address any review feedback.
8. **Squash and merge** once approved.

## Commit message format

This project follows [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` a new feature
- `fix:` a bug fix
- `docs:` documentation changes only
- `test:` adding or correcting tests
- `chore:` tooling, config, or maintenance
- `ci:` changes to CI/CD configuration

## Code style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code.
- Keep functions small and single-purpose.
- Add type hints where practical.

## Running tests locally

```bash
pip install -r requirements-dev.txt
pytest -v
```

## Code of conduct

Be respectful and constructive in all interactions.