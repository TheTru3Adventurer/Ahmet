print("""(+) (1) Toplama
(-) (2) Çıkarma
(/) (3) Bölme
(*) (4) Çarpma""")

a=int(input("Please enter a number: "))
b=int(input("Enter a number: "))
number=int(input("Please select the numbers that have given:1,2,3 or 4 \n="))
if(number)==1:
    print(a+b)
elif(number)==2:
    print(a-b)
elif(number)==3:
     print(a/b)
elif(number)==4:
    print(a*b)
else:
    print("You've entered a wrong number try again: ")

