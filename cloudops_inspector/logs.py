"""Log file scanning."""
from dataclasses import dataclass, field


@dataclass
class LogScanResult:
    error_count: int = 0
    warning_count: int = 0
    last_errors: list = field(default_factory=list)


def scan_log(path: str, max_errors_shown: int = 5) -> LogScanResult:
    """Scan a log file for ERROR/WARNING lines."""
    result = LogScanResult()
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if "ERROR" in line:
                result.error_count += 1
                result.last_errors.append(line.strip())
            elif "WARNING" in line:
                result.warning_count += 1
    result.last_errors = result.last_errors[-max_errors_shown:]
    return result
