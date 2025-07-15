customer_id= int(input("Enter customer ID: "))
customer_name = input("Enter customer name: ")
is_premium_input = input("Is the customer a premium member? (yes/no): ")
is_premium = is_premium_input=="yes"
year_value = float(input("Enter the year value: "))
deal_stage = input("Enter the deal stage either Proposal/Negotiation/Closed: ")
deal_value = float(input("Enter the deal value: "))
discount_rate = 0.0
if is_premium:
    discount_rate = 0.1
elif is_premium == False and year_value >= 3:
    discount_rate = 0.05
else:
    discount_rate = 0.0
match deal_stage:
    case "Proposal":
        discount_rate += 0.02
    case "Negotiation":
        discount_rate += 0.03
    case "Closed":
        discount_rate += 0.05
    case _:
        discount_rate += 0.0
discount_amount = deal_value * discount_rate
final_deal_value = deal_value - discount_amount
print("===== CRM Deal Discount Calculator =====")
print(f"Customer ID: {customer_id}")
print(f"Customer Name: {customer_name}")
print(f"Is Premium Member: {is_premium}")
print(f"Year Value: {year_value}")
print(f"Deal Stage: {deal_stage}")
print(f"Deal Value: {deal_value}")
print(f"Discount Amount: {discount_amount}")
print(f"Final Deal Value: {final_deal_value}")
print("=========================================")

