f =open('number' , 'w')
f.write('123321')
f.close();

f=open('number' , 'r+')
some_list=list(f.read())
print(some_list);
f.close()
is_palindrome =True
for i in range(int(len(some_list)/2)) :
    if some_list[i] != some_list[len(some_list)-i-1]:
        is_palindrome=False;
if is_palindrome:
    f=open('number', 'a')
    f.write('YES')
    f.close()
else:
    f =open('number', 'w')
    for i in range(len(some_list)):
        f.write('0')
