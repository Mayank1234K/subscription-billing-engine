def evaluate_status(row):
    usage = row['total_usage_gb']
    limit = row['usage_limit_gb']
    status = row['status']

    if status == "CANCELLED":
        return "CANCELLED"

    if usage > 1.5 * limit:
        return "SUSPENDED"

    if status == "SUSPENDED" and usage <= limit:
        return "ACTIVE"

    return status