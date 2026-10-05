"""Tests for disk inspection."""
from cloudops_inspector.disk import DiskUsage, check_threshold


def test_check_threshold_exceeds():
    usage = DiskUsage(mount="C:\\", total_gb=100, used_gb=90, percent_used=90.0)
    assert check_threshold(usage, 80.0) is True


def test_check_threshold_under():
    usage = DiskUsage(mount="C:\\", total_gb=100, used_gb=50, percent_used=50.0)
    assert check_threshold(usage, 80.0) is False


def test_check_threshold_exact_boundary():
    usage = DiskUsage(mount="C:\\", total_gb=100, used_gb=80, percent_used=80.0)
    assert check_threshold(usage, 80.0) is True


def test_check_threshold_json_serializable():
    """Confirm DiskUsage fields are plain types that json.dumps can handle."""
    import json
    usage = DiskUsage(mount="C:\\", total_gb=100.0, used_gb=90.0, percent_used=90.0)
    payload = {
        "mount": usage.mount,
        "total_gb": usage.total_gb,
        "used_gb": usage.used_gb,
        "percent_used": usage.percent_used,
    }
    # Should not raise
    json.dumps(payload)