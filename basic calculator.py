def calc(num_1,oper,num_2):
    if num_2=="0" and oper=="/":
        print("You can't divide by zero")
    elif oper== "+":
        print(float(num_1)+float(num_2))
    elif oper=="*":
        print(float(num_1)*float(num_2))
    elif oper=="-":
        print(float(num_1)-float(num_2))
    elif oper=="/":
        print(float(num_1)/float(num_2))
    else:
        print("I can't do that")
    

print("Use this calculator to add, subtract, multiply, or divide \ntwo numbers. Put each symbol on a different line.")
num_1=input("")
oper=input("")
num_2=input("")    
calc(num_1,oper,num_2)
