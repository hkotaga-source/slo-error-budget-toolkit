#!/usr/bin/env python3
"""Simple Error Budget Calculator"""

import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculate remaining error budget")
    parser.add_argument("--slo", type=float, required=True, help="SLO percentage e.g. 99.9")
    parser.add_argument("--window-days", type=int, default=30, help="Window in days")
    parser.add_argument("--error-rate", type=float, required=True, help="Observed error rate e.g. 0.002")
    args = parser.parse_args()

    allowed_error_rate = (100 - args.slo) / 100
    total_minutes = args.window_days * 24 * 60
    budget_minutes = total_minutes * allowed_error_rate
    consumed_minutes = total_minutes * args.error_rate
    remaining = max(0, budget_minutes - consumed_minutes)

    print(f"SLO                : {args.slo}%")
    print(f"Window             : {args.window_days} days")
    print(f"Allowed error rate : {allowed_error_rate*100:.3f}%")
    print(f"Error budget       : {budget_minutes:.1f} minutes")
    print(f"Consumed so far    : {consumed_minutes:.1f} minutes")
    print(f"Remaining budget   : {remaining:.1f} minutes")

if __name__ == "__main__":
    main()
