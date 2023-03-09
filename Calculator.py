# Add numbers
def add(a,b):
    return a+b

# Substract numbers
def sub(a,b):
    return a-b

# Multiply numbers
def mul(a,b):
    return a*b

# Divide numbers
def div(a,b):
    return a/b

# Mod function
# def mod(a,b):
#  return a%b

# Selecting Operation
print("select operation")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

while True:
    #Input from user
    Select = input("Enter(1/2/3/4):")

    # check if select from this
    if Select in ('1','2','3','4'):
          try:
                number1 = float(input("Enter first number: "))
                number2 = float(input("Enter second number: "))
          except ValueError:
                print("Invalid input.....Please enter a valid number.")
                continue
   

          if Select =='1':
            print(number1, "+", number2, "=", add(number1,number2))

          elif Select =='2':
            print(number1, "-", number2, "=", sub(number1,number2))

          elif Select =='3':
            print(number1, "*", number2, "=", mul(number1,number2))

          elif Select =='4':
            print(number1, "/", number2, "=", div(number1,number2))

          else:
            print("Invalid Input")    

            
        