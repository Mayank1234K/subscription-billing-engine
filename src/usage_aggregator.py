import pandas as pd
import logging

logger = logging.getLogger(__name__)

def aggregate_usage(usage_df):
    usage_df['usage_date'] = pd.to_datetime(usage_df['usage_date'], errors='coerce')

    # Filter March 2024 only
    usage_df = usage_df[
        (usage_df['usage_date'].dt.month == 3) &
        (usage_df['usage_date'].dt.year == 2024)
    ]

    usage_df = usage_df.dropna(subset=['usage_date'])

    usage_df['data_used_gb'] = pd.to_numeric(usage_df['data_used_gb'], errors='coerce').fillna(0)

    result = usage_df.groupby('subscription_id')['data_used_gb'].sum().reset_index()
    result.rename(columns={'data_used_gb': 'total_usage_gb'}, inplace=True)

    return result