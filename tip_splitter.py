'''
Henry Petzinger
IS 303 - A01

Tip Splitter
This program splits a restaurant bill among friends with a tip

Inputs:
-restaurant name, 
-bill amount, 
-tip percentage, 
-number of people

Processes:
Total with tip = bill * (1 + tip%/100); per person = total / people

Outputs:
Print the name of the person next to the total bill amount for each person

'''

restaurant_name = input("What is the restaurant name?")
bill_amount = float(input("What is the bill amount?"))
tip_percentage = float(input("WHat is the tip percentage?"))
number_of_people = int(input("How many people bought food?"))

total_with_tip = bill_amount * (1 + tip_percentage/100)
per_person = total_with_tip / number_of_people

print(f"{restaurant_name} | Total with tip: ${total_with_tip:.2f} | Each person owes: ${per_person:.2f}")



