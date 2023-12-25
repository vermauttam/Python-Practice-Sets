##Square of the number less than the number##

# num=int(input("Enter any Number: "))
# while num>0:
#     num=num-1
#     print(num**2)



# num=0
# count=0
# for num in range(1,10):
#     if num%2==0:
#         count=count+1
#         num=num+1
#         continue
#     print(num)



# num=1
# count=0
# for i in range(0,10):
#     num=num+2
#     count=count+1
#     print(count  ,  num)








# num=0
# count=0
# while num<11:
#     if num%2!=0:
#         print(num,"is odd number")
#         num+=1
#     else:
#         num+=1    



# num=int(input("Enter any Number: "))



# num=0
# count=0
# num=int(input("Enter any number > 150: "))
# while num>150:
#     if num%3==0:
#         print('"Fizz"')
#     elif num%5==0:
#         print('"Buzz"')
#     elif num%3==0 and num%5==0:
#         print('"FizzBuzz"')
#     else:
#         print('"Invalid input"')

        


        

# num=int(input("Enter any Number: "))
# count=0
# while num>10:
#     num=num/3
#     count=count+1
#     print(num)
# print(f"Your number has been divided {count} times")





# num=int(input("Enter the number to obtain it's Factorial: "))
# factorial=1
# if num<0:
#     print("Factorial cannot be Obtained")
# elif num==0:
#     print(f"Factorial of {num} is 1")    
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(f"Factorial of {num} is ",factorial)        




# num=int(input("Enter any Number: "))
# p=1
# for i in range(1,num+1):
#     p=p*i
# print(p)



# num=int(input("Enter any Number: "))
# a=num%10
# b=(num//10)-10*(num//100)
# c=num//100
# print(a+b+c)




# num=int(input("Enter any Number: "))
# a=num%10
# b=(num//10)-10*(num//100)
# c=num//100
# print(a,b,c)


# for num in range(2,10):
#     for x in range(2,num):
#         if num%x==0:
#             print(f"{num} is not a Prime number")
#             break
#     else:
#         print(f"{num} is a Prime number")



# num=int(input("Enter any number: "))
# if num[-1]









# num="123"  
# sum=0
# for i in num:
#     sum=sum+int(i)
# print(sum)



# num=input("Enter any number to get sum: ")
# sum=0
# for i in num:
#     sum=sum+int(i)
# print(sum)    





# num="153"
# sum=0
# for i in num:
#     sum+=int(i)**len(num)
# if sum==int(num):
#     print("It is an Armstrong number")
# else:
#     print("It is not an Armstrong number")        






# num=int(input("Enter any Number:  "))
# num_1=num
# i=0
# while num>0:
#     digit=num%10
#     i=i*10+digit
#     num=num//10
# if num_1==i:
#     print(f"{num_1} is a Palindrome")
# else:
#     print(f"{num_1} is not a Palindrome")        






# num=int(input("Enter no: "))
# rev=0
# while num>0:
#     remainder=num%10
#     rev=(rev*10)+remainder
#     num=num//10
# print(rev)    















# secret_number=123123
# num=int(input("Enter the Secret number: "))
# while num!=secret_number:
#     num=int(input("Try Again, Enter the Secret number :  "))
#     if num==secret_number:
#         print('"Well done, muggle! You are free now."')
#     elif num!=secret_number:
#         print('"Ha ha! You\'re stuck in my loop"')














# status_bike=["ok","ok","ok","faulty","ok","ok"]
# for status in status_bike:
#     if status=="faulty":
#         break
# print(f"Bike is {status}")







# num=int(input(">>"))
# while num>0:
#     num=num-1
#     print(num*num)


# num=1
# count=0
# for i in range(0,10):
#     num=num+2
#     count=count+1
#     print(count , f">:{num} ")






# factorial=1
# num=int(input("Enter any number to find its Factorial: "))
# if num=="0":
#     print("Factorial is 1")
# elif num<0:
#     print("Factorial cannot be Obtained")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(f"Factorial of {num} is {factorial}")            





# for num in range(2,10):
#     for x in range(2,num):
#         if num%x==0:
#             print(f"{num} is not a Prime number")
#             break
#     else:
#         print(f"{num} is a Prime number")        



# num=int(input("Enter no: "))
# rev=0
# while num>0:
#     remainder=num%10
#     rev=(rev*10)+remainder
#     num=num//10
# print(rev)    



# num=int(input("Enter any number: "))
# sum_digits=0
# while num>0:
#     digit=num%10
#     sum_digits+=digit
#     num=num//10
# print(sum_digits)    





# num="153"
# sum=0
# for i in num:
#     sum+=int(i)**len(num)
# if sum==int(num):
#     print("Palindrome")
# else:
#     print("Not Palindrome")        





# num=int(input("Enter any Number: "))
# s=0
# for i in range(1,num):
#     if num%i==0:
#         s+=i
# if s==num:
#     print(f"{num} is perfect")
# else:
#     print(f"{num} is not Perfect")            







# sum of digits of a number
# reverse of a number
# armstrong number
# palindrome number
# perfect number
# prime number
# factorial of a number




# sum=0
# num=int(input("Enter any number: "))
# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
# print(f"Sum of the digit is {sum}")    




# rev=0
# num=int(input("Enter any number: "))
# while num>0:
#     remainder=num%10
#     rev=(rev*10)+remainder
#     num=num//10
# print(f"Reverse is {rev}")    



# factorial=1
# num=int(input("Enter any number to obtain Factorial: "))
# for i in range(1,num+1):
#     factorial=factorial*i
#     if num==0:
#         print("Factorial of 0 is 1")
#     elif num<0:
#         print("Factorial cannot be Obtained")   
# else:         
#     print(f"Factorial of {num} is {factorial}")



# for num in range(2,10):
#     for x in range(2,num):
#         if num%x==0:
#             print(f"{num} is not a Prime number ")
#             break
#     else:
#         print(f"{num} is a Prine number")        


