
def calculate_average_order_value(orders):
    if not isinstance(orders, list) or not orders:
        return 0.0

    total = 0.0
    valid_orders = 0

    for order in orders:
        try:
            if order.get("status") != "cancelled":
                total += float(order.get("amount", 0))
                valid_orders += 1
        except (TypeError, ValueError):
            continue

    return total / valid_orders if valid_orders > 0 else 0.0
