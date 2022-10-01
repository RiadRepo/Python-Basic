n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)
sc = None

for num in arr:

    if num == mx:
            pass
    elif sc == None:
            sc = num

    elif num > sc:
            sc = num


print(sc)

# finding in list

# Result =[]
# scorelist = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     Result+=[[name,score]]
#     scorelist+=[score]
# b=sorted(list(set(scorelist)))[1]
# print(b)
# for a,c in sorted(Result):
#     print(Result)
#     if c==b:
#         print(a)
