import random

upperCase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowerCase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbol=[ "!","@","#","$","~","%","^","*","&","=","0",",">","<",",",","/","?" ]
numbers=["1","2","3","4","5","6","7","8","9","0"]

all= upperCase + lowerCase + symbol + numbers


print("Welcome to password generator 😀")
print("Maximum number of character should below 30")
digits=int(input("Entre the number of digits for your password:"))

length = digits

password="".join(random.sample(all,length))
print("The password for you is:",password)


 
