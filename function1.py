#Function : Generate an event ticket
def calculate_ticket_price(category):
    if category == "standard":
        return 60.00
    elif category == "premium":
        return 90.00
    elif category == "vip":
        return 120.00
    else:
        return "Invalid category"

tickect_price = calculate_ticket_price("premium")
print("tickect_price:", tickect_price)