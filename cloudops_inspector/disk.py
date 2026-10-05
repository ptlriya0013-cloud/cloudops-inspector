"""Disk usage inspection."""
import shutil
from dataclasses import dataclass


@dataclass
class DiskUsage:
    mount: str
    total_gb: float
    used_gb: float
    percent_used: float


def get_disk_usage(mount: str = "C:\\") -> DiskUsage:
    """Return disk usage stats for a given mount/drive."""
    total, used, free = shutil.disk_usage(mount)
    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    percent_used = round((used / total) * 100, 1)
    return DiskUsage(mount=mount, total_gb=round(total_gb, 2),
                      used_gb=round(used_gb, 2), percent_used=percent_used)


def check_threshold(usage: DiskUsage, threshold: float) -> bool:
    """Return True if usage exceeds the given threshold percent."""
    return usage.percent_used >= threshold