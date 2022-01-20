Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=int(input("enter a number"))
if n%2!=0:
    print("Wierd")
elif n%2==0 and 2<=n<=5:
    print("Not Wierd")
elif n%2==0 and 6<=n<=20:
    print("Wierd")
elif n%2==0 and n>20:
    print("Not wierd")
else:
    print("enter Only numebers")
    
