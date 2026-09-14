units = int(input("Enter units: "))

if units <= 100:
    cost = 10 * units
    print("Cost of the units:", cost)

elif units > 100 and units <= 300:
    cost = 15 * units
    print("Cost of the units:", cost)

else:
    cost = 20 * units
    print("Cost of the units:", cost)