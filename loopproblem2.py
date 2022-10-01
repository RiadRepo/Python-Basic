#pattern 1
row =int(input("enter your row number"))

count =0

for i in range (0, row) :
    for j in range (0, row-i-1) :
        print(end=" ");

    count = count + 1
    for k in range (0, count+i) :
        print("*" ,end ="");

    print(" ")
#pattern 2

row =int(input("Enter the number of row"))

count=0

for i in range (0 , row) :
    for j in range (0, row -i-1) :
        print(end=" ");

    count =count +1
    for k in range(0, count) :
        print("*" , end ="");

    print(" ")
