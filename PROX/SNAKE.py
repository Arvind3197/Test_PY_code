'''

PYTHON PRACTICE

==============================================================>DUMS
x = 9
y = 10

if x < y:
    print('you are right')

else:
    print('you are wrong')

input =('the king: ')
x = 'arvind'
y = print('the king: '+ x) 

x=type(str('5'))
print (x)

age = 70
student = 'yes'

if age >= 60 or student=='yes':

no_of_persons = int(input('Enter how many persons: '))

if no_of_persons > 2:
    print ('not allowed')
else:
    print('allowed')
'''
'''
name = str(input('enter your name: '))

if name == ('arvind'):
    print('welcome king')
else:
    print ('your are not a king')
 '''
'''
i = 1
while i < 6:
  print(i)
  i += 1
'''
'''
======================================================================> FROM W3
'''

###########list comprehension

padmi = ["skandan","murugan","subramani"]
sara = []

for x in padmi:
  if "d" in x:
    sara.append(x)

print(sara)

mandu = [x for x in padmi if "s" in x]

print(mandu)

jodu = [a for a in padmi if a != "skandan"] #!= checks true value and leave that element and makes a new list to print

print(jodu)

terror = [x for x in range(50) if x <= 25] # >, <, >=, <=

print(terror)

ludo = [x.upper() for x in padmi]

print(ludo)

apple = ["murugan" for x in padmi]

print(apple)

orange = [x if x != "skandan" else "saravanabhava" for x in padmi] # if skandan is true the line will replace saravaabhava in place of skandan

print(orange)

#Sort list

padmi.sort()

print(padmi)

num = [100, 50, 65, 82, 23]
num.sort()

print(num)

num.sort(reverse = True) # both num and padmi

print(num)

padmi.reverse()

print(padmi)

#copy list

dupli = padmi.copy()

print(dupli)

#Join list

padmi2 = padmi + num
padmi.extend(num)
  

print(padmi2)
print(padmi)

###############TUPLES

rod = ('sladar','willow','tidehunter','pudge','bountyhunter')
i = 0
while i < len(rod):
  print(rod[i])
  i = i + 1

for x in range(len(rod)):
    print(rod[x])

'''
arvind = input('enter your name: ')

i = 0
while i < len(arvind):
  print(arvind[i])
  i = i + 1
'''

#####SETS

#####Dictionaries

################### IF..ELSE

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#or
a = 5
b = 33
c = 4
if a > b or a > c:
  print("At least one of the conditions is True")

#####functions
'''
def my_function():
  print("Hello from a function")

my_function()

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
'''
import DAWN
print(DAWN.my_function(5, 6, c=7, d=8))


##Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results: ")

tri_recursion(6)





