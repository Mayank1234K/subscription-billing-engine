from src.billing_engine import calculate_bill

def test_bill_without_overage():
    row = {'total_usage_gb': 50, 'usage_limit_gb': 100, 'monthly_fee': 200, 'status': 'ACTIVE'}
    bill, overage = calculate_bill(row)
    assert bill == 200

def test_bill_with_overage():
    row = {'total_usage_gb': 150, 'usage_limit_gb': 100, 'monthly_fee': 200, 'status': 'ACTIVE'}
    bill, overage = calculate_bill(row)
    assert bill == 700

def test_suspended_subscription_billing():
    row = {'total_usage_gb': 200, 'usage_limit_gb': 100, 'monthly_fee': 200, 'status': 'SUSPENDED'}
    bill, _ = calculate_bill(row)
    assert bill == 200

def test_cancelled_subscription_billing():
    row = {'total_usage_gb': 200, 'usage_limit_gb': 100, 'monthly_fee': 200, 'status': 'CANCELLED'}
    bill, _ = calculate_bill(row)
    assert bill == 0