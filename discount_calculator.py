# E-commerce Discount Calculator

amount = float(input("Enter the purchase amount ($): "))

if amount < 100:
    discount = 0
elif amount <= 500:
    discount = amount * 0.10
else:
    discount = amount * 0.20

final_amount = amount - discount

print("\n----- Bill Summary -----")
print(f"Purchase Amount: ${amount:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final Amount to Pay: ${final_amount:.2f}")
