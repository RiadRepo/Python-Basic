#key word argument -end. using this we can print same line output


print("hello",end=" ");
print('hello');
 #keyword agrument -sep .using this we can separated with and symbol output

print("print with sep" );
print('a','b','c' ,sep="/");

#global scope

def funtion() :
    c=10;
    #print(c);
#funtion()
#print(c); #here didnot access c .cause its a local veriable but we want to try access as a global veriable
def f():
    global a;
    a=10;
f();
print(a);
