# 1+2+3+4+5+6+7+8+9+....+n
n = int(input("enter your Number "))  # 5
sum = 0

for i in range(1, n + 1, 1):
    sum += i
print(sum)  # 15

# 2+4+6+....+n

x = int(input("Enter Your Input Number "))
sum1 = 0

for y in range(2, x + 1, 2):
    sum1 += y
print(sum1)


# 1+3+5+...+n

a = int(input("enter your last number "))

sum2 = 0

for b in range(2, a + 1, 2):
    sum2 += b
print(sum2)

# 4+8+12+..+n

m = int(input("Enter Your Number "))
sum3 = 0

for l in range(4, m + 1, 4):
    sum3 += l
print(sum3)

# 1^2+2^2+3^3+....+n^2

w = int(input("enter your number :"))
sum4 = 0
for u in range(1, w + 1, 1):
    sum4 += u * u
print(sum4)

#2^2 + 4^2 + 6^2 + 8^2 + 10^2+...+n^2

p = int(input("enter your number :"))
sum5 = 0
for q in range(2, p + 1, 2):
    sum5 += q * q
print(sum5)

# 1+ 1/2 +1/3 +1/4+.....+1/n

E = int(input("enter your last number"))
sum6 = 0

for f in range(1, E + 1, 1):
    sum6 += 1 / f
print(sum6)

# 1*2*3*4*....*n
R = int(input("enter your Number sum number"))
sum7 = 1

for t in range(1, R + 1, 1):
    sum7 = sum7 * t
print(sum7)
