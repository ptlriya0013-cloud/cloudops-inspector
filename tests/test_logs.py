"""Tests for log scanning."""
import tempfile
import os
from cloudops_inspector.logs import scan_log


def _write_temp_log(lines):
    fd, path = tempfile.mkstemp(suffix=".log")
    with os.fdopen(fd, "w") as f:
        f.write("\n".join(lines))
    return path


def test_scan_log_counts_errors_and_warnings():
    path = _write_temp_log([
        "INFO: starting up",
        "ERROR: disk full",
        "WARNING: low memory",
        "ERROR: connection timeout",
    ])
    try:
        result = scan_log(path)
        assert result.error_count == 2
        assert result.warning_count == 1
    finally:
        os.remove(path)


def test_scan_log_limits_last_errors():
    lines = [f"ERROR: failure {i}" for i in range(10)]
    path = _write_temp_log(lines)
    try:
        result = scan_log(path, max_errors_shown=3)
        assert len(result.last_errors) == 3
        assert result.last_errors[-1] == "ERROR: failure 9"
    finally:
        os.remove(path)


def test_scan_log_no_issues():
    path = _write_temp_log(["INFO: all good", "INFO: still good"])
    try:
        result = scan_log(path)
        assert result.error_count == 0
        assert result.warning_count == 0
    finally:
        os.remove(path)