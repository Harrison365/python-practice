#theres no var let or const in python

x=6
str = 'hello \'Joe\''
print(x)
print(type(x))
print(str)
print(len(str)) #len() is like .length
# print(len(x)) wont work as x is a number 
print(type(6.0))
print(type(6))
print(6==6.0)
#True and False have capitals in python

if x>4:
    print("ok","see") #4 spaces show whats inside the curley braces (but we dont write curley braces)

if x>20:
    print("big x")
elif x>5:
    print("yeeeee")
else:
    print("else this happens")


if x:
    print("truuthy")

# truthy stuff still applies

# None == null and is falsey

# not is the same as ! ... so 
if not 0:
    print("not 0 is truthy")