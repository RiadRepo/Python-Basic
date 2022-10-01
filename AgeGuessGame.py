import random as r
secret_age =  r.randint (1,10)
flag=False;

def Game_func(guess_age,secret_age):
    if guess_age<secret_age:
       return "Too Low";
    elif guess_age>secret_age:
       return "Too High";
    else:
       return "correct";

for i in range(1,6):
    print('Take a guess .You have '+str(6-i)+" guesses left");
    guess_age=int(input())
    if Game_func(guess_age,secret_age) == "correct" :
        print('you won the game!');
        flag =True;
        break;

if not flag:
    print('you lost the game!');


