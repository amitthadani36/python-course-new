car_variant = "z2E petrol"
car_price = 2000000
time_period = 5
rate_of_interest = 8
initial_down_payment = 500000
simple_interest = (car_price - initial_down_payment) * rate_of_interest * time_period / 100
total_amount = car_price - initial_down_payment + simple_interest
monthly_installment = total_amount / (time_period * 12)
print("======================")
print(f"Car Variant: {car_variant}")
print(f"Car Price: {car_price}")
print(f"Time Period: {time_period} years")
print(f"Rate of Interest: {rate_of_interest}%")
print(f"Initial Down Payment: {initial_down_payment}")
print(f"Simple Interest: {simple_interest}")
print(f"Total Amount Payable: {total_amount}")
print(f"Monthly Installment: {monthly_installment}")