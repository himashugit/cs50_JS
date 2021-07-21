import sys # module in python for system

try: # this we use for in case we give the input as string (hello) and give error as ValueError
  x = int(input("x: "))
  y = int(input("y: "))
except ValueError:
    print("Error : invalid input")
    sys.exit(1)

try: # this we use in case we're providing value as 0
  result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")