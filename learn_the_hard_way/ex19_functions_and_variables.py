def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"And {box_of_crackers} boxes of crackers!")
    print("Enough for a party!\n")


print("We can give function numbers directly:")
cheese_and_crackers(20, 33)

print("Or we pass variables:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside function input variables:")
cheese_and_crackers(10 ** 2.0, 5 + 6)

print("Combine variables and math:")
cheese_and_crackers(amount_of_cheese * 3, amount_of_crackers / 2)
