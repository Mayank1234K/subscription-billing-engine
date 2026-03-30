from src.status_engine import evaluate_status

def test_active_to_suspended_transition():
    row = {'total_usage_gb': 200, 'usage_limit_gb': 100, 'status': 'ACTIVE'}
    assert evaluate_status(row) == 'SUSPENDED'

def test_suspended_to_active_transition():
    row = {'total_usage_gb': 50, 'usage_limit_gb': 100, 'status': 'SUSPENDED'}
    assert evaluate_status(row) == 'ACTIVE'

def test_cancelled_status_unchanged():
    row = {'total_usage_gb': 200, 'usage_limit_gb': 100, 'status': 'CANCELLED'}
    assert evaluate_status(row) == 'CANCELLED'