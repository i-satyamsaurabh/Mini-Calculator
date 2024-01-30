print("Hello, You're Welcome! ")
f=int(input("Enter your First Number :"))
o=(input("Enter your Operator from (+,-,*,/,%):"))
s=int(input("Enter your Second Number :"))

if o=="+":
    print("Your output is", f+s)
elif o=="-":
    print("Your output is", f-s)
elif o=="*":
    print("Your output is", f*s) 
elif o=="/":
    print("Your output is", f/s)
elif o=="%":
    print("Your output is", f%s)
else:
    print("Invalid Operation")                   



    