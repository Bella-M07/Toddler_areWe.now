c = int(input("Enter number 1: "))
d = int(input("Enter number 2: "))
operation = input("Enter the operation +, -, *, / you want to perform: ")

if(operation == '+'):
    print("The value of", c, operation, d, "is",c+d)
elif(operation == '-'):
    print("The value of", c, operation, d, "is",c-d)
elif(operation == '*'):
    print("The value of", c, operation, d, "is",c*d)
elif(operation == '/'):
    if(d==0):
        print("eorror.")
    else: print("The value of", c, operation, d, "is",c/d)
else: print("error, bro.")