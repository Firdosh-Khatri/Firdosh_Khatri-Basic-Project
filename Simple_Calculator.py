num_1=int(input("Enter a number "))
num_2=int(input("Enter a number "))
mat_op=input("Enter any mathematical operator ")
if mat_op=="-":
    print(num_1,"-", num_2,"=", num_1-num_2)
elif mat_op=="+":
    print(num_1,"+", num_2,"=", num_1+num_2)
elif mat_op=="*":
    print(num_1,"*", num_2,"=", num_1*num_2)
elif mat_op=="/":
    if num_2!=0:
     print(num_1,"/", num_2,"=", num_1/num_2)
    else:
     print("The number is not divisible by zero")
else:
   print("Error, check the number or operators")
