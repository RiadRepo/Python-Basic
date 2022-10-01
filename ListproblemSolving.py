#leaner search
"""
a= [1,3,4,55,6]

def leaner_search(list , Value):
    for i in range(len(list)) :
        if list[i]==Value:
            return "found"
    if i==len(list)-1:
        return "not Found"

print(leaner_search(a , 4))
print(leaner_search(a , 5))
"""
#binary search
"""
a=[464,48,4747]

def binary_search(list, value) :
     if value>list[-1] :
         return 'Not found'
     first =0
     last = len(list)-1
     while first<=last :
         mid =(first+last)//2
         if list [mid] ==value:
             return "found"
         elif list [mid] >value :
             first =mid+1
         elif list[mid]<value :
             first =mid -1
     if first> last :
         return 'not found'


print(binary_search(a,48))
print(binary_search(a,40))
"""

#print Odd number in list
"""
a= [1,3,4,55,6]
def print_odd(list):
    new_list=[]
    for i in range (len(list)):
          if list[i]%2!=0:
              new_list.append(list[i])
    return new_list
print(print_odd(a))

"""
#central avg

a=[1,2,3,4,5]
def centered_avg(list):
    sum=0
    count=0

    for i in range (1,len(list)-1):
        sum=sum +list[i]
        count =count+1
    return sum/count
print(centered_avg(a))
