car_variant = "z2E petrol"
car_price = 2007695
time_period = 5
rate_of_interest = 8
initial_down_payment = 500000
loan_amount = car_price - initial_down_payment
months = time_period * 12
monthly_interest_rate = rate_of_interest / (12*100)
emi = (loan_amount * monthly_interest_rate * ((1+monthly_interest_rate) ** months)) / (((1+monthly_interest_rate) ** months) - 1)
total_amount = emi* time_period *12
print("======================")
print(f"Car Variant: {car_variant}")
print(f"Car Price: {car_price}")
print(f"Time Period: {time_period} years")
print(f"Rate of Interest: {rate_of_interest}%")
print(f"Initial Down Payment: {initial_down_payment}")
print(f"loan amount: {loan_amount}")
print(f"Total Amount Payable: {total_amount}")
print(f"Monthly Installment: {emi}")