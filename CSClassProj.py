# convert fahrenheit into celsius. this is supposed to be "easy" but okay
# define a function first!
# this is done by Umar
CHOICE = str(input("What do you want to convert to? (Celsius or Fahrenheit) "))
TEMPINPUT = int(input("Enter The Temperature --> "))
if CHOICE == "Celsius":
    print("Temperature in Fahrenheit",(TEMPINPUT*(9/5))+32)
elif CHOICE == "Fahrenheit":
    print("Temperature in Celsius",(5/9)*(TEMPINPUT-32))
else:
        print("Sorry, Something went wrong. Please try again.")