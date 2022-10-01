#normalList
"""
a=['a','b','c']
b=[12,36,5]
z=[3.4666,6.5]
print(a[2]) #individual showing data
"""
#nestedList
"""
a=[['a','b','c'],['Riad','Rafyet','Rakib'],[12,4.5,777]]

print(a[1][0]); #[Total list index][individual index]

"""

#negative indexes
"""
p=[1,2,3,4]
print(p[-1]) #its starting with last list item. here -1 means 4
print(p[-2])
"""

#sublist and slicing
"""
q=[1,2,3,4,5]
print(q[0:4])  #q=[start_index :end_index]
print(q[0:-2]) # here start with 0 index and end index is -2
print(q[1:-1])
print(q[:])  # print all index
print(q[1:])  # print 1 index to last
print(q[:4]) # print starting index to 3 rd no index
"""
#listing concatenation
"""
a=['a','b','c']
b=[1,3,4,4]
ab=a+b;
print(ab)

x=['p','q','s']
new_x=x*2;  #double print
print(new_x)
"""

#listdelete
"""
p=['a','b',0,9]
del p[1]
print(p)

p.remove(0)
print(p)
"""
#searching Index on list
"""
place_Visited=['india','nepal', 'malaysia','Bhutan','usa']
print(place_Visited.index('Bhutan'))
"""
#adding on list
"""
place_Visited=['india','nepal', 'malaysia','Bhutan','usa']
place_Visited.append('Africa');  #adding on last index
print(place_Visited);

place_Visited.insert(2, 'Uk')
print(place_Visited)
"""
#sorting list
"""
place_Visited=['india','nepal', 'Malaysia','Bhutan','usa']
place_Visited.sort()
print(place_Visited)
place_Visited.sort(key=str.lower , reverse=True)
print(place_Visited)
"""
#assuming multiple values at once
"""
chocolate_milk_shake =['chocolate','milk','ice','blender']
x,y,z,q=chocolate_milk_shake
print(x)
print(x,y,z,q)
"""
#string are list too
"""
a= "whats your name? "
print(a[0])
"""
#_______________Tuple__________________
#tuple data type didnot modify .its look like a list , behaviour like string
#simple tuple
"""
tup =(1 ,2 ,3 ,'hello',47574.4)
print(tup);
print(type(tup))
print(tup[4])
print(tup[:4])  #tuple slice
"""
#tuple convert to list
"""
new_list= list(tup)
print(new_list)
print(type(new_list))
#list converted to tuple
T = tuple(new_list)
print(T)
print(type(T))
"""
#refrenceListing
"""
import copy as cp
def f (some_list):
    some_list.append('ok')

x=[1,2,3]
s=cp.copy(x) #a copy of the list is made
f(x)
print(x)
print(s)
"""

#---------------------Dictionary-------------------
#here we can create custom index i mean custom key
#simple dictionary
my_stuff ={'book':'Cookbook' , 'phone':'iphone' ,'Home':'Bangladesh'}
print(my_stuff['book'])  # searching with index

x={0:100, 18:36,56:89}
print(x[18])

#index difference list and dictionary

x={0:100,1:200}
y={1:200,0:100}
print(x==y)  #true

a=[1,2,3]
b=[3,2,1]
print(a==b)  #false

#Dictionary Concatenating

D={'a':100 ,'b':200}
E={'c':300, 'd':400}

new_dec=D.copy();
new_dec.update(E)
print(new_dec)
#print values, keys,items
identity ={ "name" : 'riyad', 'age':'21' , 'job':'student'}
for i in identity.values():
    print(i)

for j in identity.keys():
    print(j)

for q in identity.items():
   print(q)

#convert to a list
M=list(identity.items())
print(M)
#using two veriable
for k , v in identity.items():
    print('key ' + k +' value '+v)

#using in function
print('Akil' in identity.values()) #false
print('riyad' in identity.values()) #true


#get method

print(str(identity.get('name' ,"DEFAULT"))) # if available then give us value,not available then Default
print(str(identity.get('Height' ,"Default")))

#setdefault()
print(identity.setdefault('name','cosmos'))
print(identity.setdefault('height', '6ft'))  #if if key available then given value . if not available then added and given value
print(identity)

