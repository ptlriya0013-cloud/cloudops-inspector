"""CLI entry point for cloudops-inspector."""
import argparse
import json
import sys

from cloudops_inspector.disk import get_disk_usage, check_threshold
from cloudops_inspector.logs import scan_log


def main():
    parser = argparse.ArgumentParser(prog="inspect", description="cloudops-inspector CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    disk_parser = subparsers.add_parser("disk", help="Inspect disk usage")
    disk_parser.add_argument("--mount", default="C:\\", help="Mount/drive to inspect")
    disk_parser.add_argument(
        "--threshold", type=float, default=80.0,
        help="Usage percent threshold to flag",
    )
    disk_parser.add_argument("--json", action="store_true", help="Output as JSON")

    logs_parser = subparsers.add_parser("logs", help="Scan a log file")
    logs_parser.add_argument("path", help="Path to the log file")
    logs_parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.command == "disk":
        usage = get_disk_usage(args.mount)
        exceeded = check_threshold(usage, args.threshold)

        if args.json:
            print(json.dumps({
                "mount": usage.mount,
                "total_gb": usage.total_gb,
                "used_gb": usage.used_gb,
                "percent_used": usage.percent_used,
                "threshold_exceeded": exceeded,
            }))
        else:
            print(f"Mount: {usage.mount}")
            print(f"Total: {usage.total_gb} GB | Used: {usage.used_gb} GB ({usage.percent_used}%)")
            if exceeded:
                print(f"WARNING: usage exceeds {args.threshold}% threshold!")

        if exceeded:
            sys.exit(1)

    elif args.command == "logs":
        result = scan_log(args.path)

        if args.json:
            print(json.dumps({
                "error_count": result.error_count,
                "warning_count": result.warning_count,
                "last_errors": result.last_errors,
            }))
        else:
            print(f"Errors: {result.error_count} | Warnings: {result.warning_count}")
            if result.last_errors:
                print("\nLast errors:")
                for line in result.last_errors:
                    print(f"  {line}")


if __name__ == "__main__":
    main()
