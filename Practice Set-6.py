num1=int(input("Enter the marks Obtained in 100: "))
num2=int(input("Enter the marks Obtained in 100: "))
num3=int(input("Enter the marks Obtained in 100: "))

l1=[num1,num2,num3]
highest1=max(l1)

l1.remove(highest1)
highest2=max(l1)

print(f"Average of two best marks is {(highest1+highest2)/2} ")

