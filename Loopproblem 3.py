#armstrong check
digit = int(input("enter your number :"))
temp=digit
sum=0

while digit !=0 :
    digit_mod = digit % 10
    digit = digit//10
    sum = sum+digit_mod**3

if sum==temp :
    print("this number is armstrong");
else :
    print("this number is not armstrong")

