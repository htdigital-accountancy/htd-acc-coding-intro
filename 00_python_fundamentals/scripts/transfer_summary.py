"""
Worked example: summarise a small list of transfers.

Run from the terminal:
  cd 00_python_fundamentals
  python scripts/transfer_summary.py

Try changing LARGE_THRESHOLD or the filters, then re-run.

Reminder: print(...) shows a value in the terminal.
         name = value stores that value under a name (a variable).
"""

transfers = [
    {"type": "deposit", "amount": 1000.0, "currency": "USDT", "network": "TRON"},
    {"type": "withdrawal", "amount": 15000.0, "currency": "USDT", "network": "TRON"},
    {"type": "withdrawal", "amount": 100.0, "currency": "BTC", "network": "BITCOIN"},
    {"type": "deposit", "amount": 2.5, "currency": "BTC", "network": "BITCOIN"},
    {"type": "withdrawal", "amount": 8333.33, "currency": "USDC", "network": "POLYGON"},
]

LARGE_THRESHOLD = 10000.0


def is_large_transfer(transfer, threshold):
    return transfer["amount"] > threshold


def count_by_type(transfers):
    deposits = 0
    withdrawals = 0
    for t in transfers:
        if t["type"] == "deposit":
            deposits = deposits + 1
        elif t["type"] == "withdrawal":
            withdrawals = withdrawals + 1
    return deposits, withdrawals


deposits, withdrawals = count_by_type(transfers)
print(f"Deposits: {deposits}")
print(f"Withdrawals: {withdrawals}")

print(f"\nLarge transfers (amount > {LARGE_THRESHOLD}):")
for t in transfers:
    if is_large_transfer(t, LARGE_THRESHOLD):
        print(f"  {t['type']} {t['amount']} {t['currency']} on {t['network']}")
