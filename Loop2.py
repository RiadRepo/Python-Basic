#infinity loop
"""
while True :
   print('Enter Your Name ');
   name = input();
   if (True) :
    if(name=='Riad'):
       print('Hello There '+ name + " enter your password ");
       password = input()
       if (password=='hello') :
           print('thank you !' +name +'you are In')
           break;
    print('Didnot Match');
    continue;
    print('didnot found user');
    continue;
"""
#series 1+2+3+4
"""
sum=0;

for i in range(1,5) :
    sum += i;
    #sumAns=int(sum)
    print(sum );
    #print('+')

print("final Ans " ,sum)

#series 1^2+2^2+3^2+4^2

#def Square (num) :
   # return num**2

sum=0;
number = int(input("enter any value for square "))
for i in range(1,number+1):

   sum += i*i;
   print(sum);


print('Final' ,sum)


#series = 1+3+5+7

sum =0
for i in range(1,9,2) :
   sum = sum +i ;
   print(sum);
print('Final',sum)


#even series = 2+4+6+8

sum=0
for i in range (2,10,2) :
    sum= sum + i
    print(sum)
print('final', sum);
"""

#Complex Series = 1 + (1+2) + (1+2+3)+(1+2+3+4)

sum =0
for i in range (1,5) :
    for j in range (1, i+1) :
        sum = sum +j




print("final",sum);
