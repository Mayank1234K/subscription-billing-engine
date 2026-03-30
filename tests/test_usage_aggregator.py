import pandas as pd
from src.usage_aggregator import aggregate_usage

def test_no_usage_records():
    df = pd.DataFrame(columns=['subscription_id', 'usage_date', 'data_used_gb'])
    result = aggregate_usage(df)
    assert result.empty

def test_multiple_usage_records():
    df = pd.DataFrame({
        'subscription_id': [1,1],
        'usage_date': ['2024-03-01','2024-03-05'],
        'data_used_gb': [10,20]
    })
    result = aggregate_usage(df)
    assert result.iloc[0]['total_usage_gb'] == 30

def test_invalid_usage_dates():
    df = pd.DataFrame({
        'subscription_id': [1],
        'usage_date': ['invalid'],
        'data_used_gb': [10]
    })
    result = aggregate_usage(df)
    assert result.empty