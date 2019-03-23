a = input("Give me a number, and I'll print it.")
try:
    a = int(a)
    print(a)
except ValueError:
    print ("A REAL number, not a letter thingee and not a blank.")


