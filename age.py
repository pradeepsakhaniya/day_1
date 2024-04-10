Age = int(input("Enter the Age"))

if Age < 0:
    print("Invalid Age")
elif Age < 18 & Age > 0:
    print("Child")
elif Age >=18 & Age < 60:
    print("Adult")
elif Age > 60 & Age < 160:
    print("Senior Citizen")
else:
    print("Invlid Age")