# exception : it is an event detected during the normal execution and it interrupts the normal flow of the program
try:
    result = 10/5
except ZeroDivisionError as e:
    print(e)
    print("Cannot divide by zero.")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong.")
else: # else block will run if there is no exception
    print("Hurry! No exception occur")
    print(result)
finally: # finally block will always run even if there is no exception
    print("Your are doing well fellow bro")