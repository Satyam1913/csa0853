#Check Palindrome
a=input("Enter a string:")
b=a[-1::-1]
if(a==b):
    print("palindrome")
else:
    print("It is not a palindrome")
