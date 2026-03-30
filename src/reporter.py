import json

def generate_summary(df):
    summary = {
    "total_subscriptions": int(len(df)),
    "active_subscriptions": int((df['final_status'] == 'ACTIVE').sum()),
    "suspended_subscriptions": int((df['final_status'] == 'SUSPENDED').sum()),
    "cancelled_subscriptions": int((df['final_status'] == 'CANCELLED').sum()),
    "total_revenue": float(df['total_bill'].sum()),
    "average_bill": float(df['total_bill'].mean())
}
    with open("billing_summary.json", "w") as f:
        json.dump(summary, f, indent=4)