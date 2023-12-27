##Sum of digits of a number
# num="123"
# sum=0
# for i in num:
#     sum+=int(i)
# print(f"Sum of digits is {sum}")    



##Area of circle
# r=2
# area=3.14*r*r
# print(f"Area of circle is {area}")





##Best of two Test average out of three marks input
# num1=int(input("Enter the marks Obtained in 100: "))
# num2=int(input("Enter the marks Obtained in 100: "))
# num3=int(input("Enter the marks Obtained in 100: "))

# l1=[num1,num2,num3]
# highest1=max(l1)

# l1.remove(highest1)
# highest2=max(l1)

# print(f"Average of two best marks is {(highest1+highest2)/2} ")


##vowel and consonant check
# alphabet=input("Enter an Alphabet to check whether it is a Vowel or Consonant: ")
# vowels=["a","e","i","o","u","A","E","I","O","U"]
# if alphabet in vowels:
#     print("It is a Vowel")
# else:
#     print("It is a Consonant")    


##Largest among three numbera
# num1=int(input("Enter any number: "))
# num2=int(input("Enter any number: "))
# num3=int(input("Enter any number: "))

# max=num1
# if num2>num1 and num2>3:
#     max=num2
# if num3>1 and num3>num2:
#     max=num3
# print(f"Largest number is {max}")        



# #Leap year
# year=int(input("Enter the year above 1582 to check whether it is a Leap year: "))
# if year<=1582:
#     print("Year not in Gregorian Calender")
# elif year%400==0 and year%100==0:
#     print("It is a Leap year")
# elif year%4==0 and year%100!=0:
#     print("It is a Leap year") 
# else:
#     print("It is a Common year")




##accepts two characters and check whether they are equal 
# chr1=input("Enter 1st Character: ")
# chr2=input("Enter 2nd Character: ")
# if chr1==chr2:
#     print("Yes, They are Equal")
# else:
#     print("No, They are not Equal ")    


for x in range(1,5):
    for y in range(1,5):
        print("*",end=" ")
        y=y-1
print()        


