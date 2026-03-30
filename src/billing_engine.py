def calculate_bill(row):
    usage = row['total_usage_gb']
    limit = row['usage_limit_gb']
    fee = row['monthly_fee']
    status = row['status']

    if status == "CANCELLED":
        return 0, 0

    if status == "SUSPENDED":
        return fee, 0

    if usage <= limit:
        return fee, 0
    else:
        overage = usage - limit
        overage_charge = overage * 10
        return fee + overage_charge, overage