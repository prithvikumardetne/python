bill = int(input("Enter the bill amount:"))

friends = int(input("Total no of friends are : "))

Total_bill = bill + (bill * 0.02)

print(Total_bill)

individual_bill = (Total_bill / friends)

print("Individual Bill is : ",individual_bill)