bill_pretip = int(input("Enter the total bill amount, in dollars, before the tip (Ex. 100): "))
tip_amount = int(input("Enter the tip amount, in dollars (Ex. 20): "))
final_bill = bill_pretip + tip_amount
people_amount = int(input("Enter the amount of people splitting the bill (Ex. 3): "))
amount_per_person = final_bill/people_amount
amount_per_person = round(amount_per_person, 2)


print(f"\nYour final bill amount is: {final_bill}")
print(f"The amount each person is supposed to pay is: ${amount_per_person}" )