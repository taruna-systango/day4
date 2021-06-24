'''
#syntax error
if a>3

1/0

open("file.txt")
'''
print(dir(locals()['__builtins__']))

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

#raise error in pyhton
try:
  a = int(input("Enter a positive integer: "))
  if a <= 0:
    raise ValueError("That is not a positive number")
except ValueError as ve:
      print(ve)

# try with else(opetional)
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print("reciprocal",reciprocal)

#file nit found error
f = open("myfile1.txt", "w")
f.write("this is myfile")
f = open("myfile1.txt","r")
print(f.read())
try:
    p = open("day4file1.txt","r")
    print(p.read())
except:
  print("file not exist") 
finally: 
  f.close()
  p.close()

#user define exception
class BalanceException(Exception):
  pass

def check_balance():
  money = 10000
  withdraw = 2000
  try:
      balance = money - withdraw
      if(balance <= 2000):
         raise BalanceException('Insufficient Balance')
      print(balance)
  except BalanceException as bl:
      print(bl)

check_balance()
  
#enumerator function
list = ["hi","hello","namastai","goodmorning"]
for index, item in enumerate(list):
  if index % 2 == 0:
    print(f"say {item}")