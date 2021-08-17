def RepresentsInt(s):
  try: 
    int(s)
    return True
  except ValueError:
    return False

def oddOrEven(a):
  if(RepresentsInt(a)):
    a=int(a)
    if(a==0):
      print("Neither odd nor even")
    elif(a%2==0):
      print("It is an even number")
    else:
      print("It is an odd number")
  else:
    print("please enter integer")
    b=input("Enter a number:")
    oddOrEven(b)

a=input("Enter a number:")
oddOrEven(a)

