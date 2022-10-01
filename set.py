# def average(array):
#     return sum(set(array))/ len(set(array))
#
#
# n = int(input())
# arr = list(map(int, input().split()))
# result = average(arr)
# print(result)

#union

m, n = input(), set(map(int, input().split()))
i, j = input(), set( map(int, input().split()))
print(len(n|j))
