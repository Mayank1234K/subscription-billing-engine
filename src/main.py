import logging
import pandas as pd
from loader import load_csv
from usage_aggregator import aggregate_usage
from billing_engine import calculate_bill
from status_engine import evaluate_status
from reporter import generate_summary

logging.basicConfig(filename='../logs/billing.log', level=logging.INFO)

def main():
    subs = load_csv('../data/subscriptions.csv')
    usage = load_csv('../data/usage.csv')

    usage_agg = aggregate_usage(usage)

    df = pd.merge(subs, usage_agg, on='subscription_id', how='left')
    df['total_usage_gb'] = df['total_usage_gb'].fillna(0)

    # Billing
    df[['total_bill', 'overage_gb']] = df.apply(
        lambda row: pd.Series(calculate_bill(row)), axis=1
    )

    # Status
    df['final_status'] = df.apply(evaluate_status, axis=1)

    df.to_csv('../billing_output.csv', index=False)

    generate_summary(df)

if __name__ == "__main__":
    main()