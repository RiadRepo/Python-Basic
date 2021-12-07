#list 

subject=["c","c++","java","python","c#"]

print(subject)
print(subject[0])
print(subject[2:])
print(subject[-2]) #reverse
print("python" in subject) #check in list
print("c#" not in subject) #check in not list
print(subject + ["swift",28])
print(subject * 3)
print(len(subject))

subject.append("Basic")
print(subject)

subject.insert(2,"OS")
print(subject)


subject.remove("c")
print(subject)

subject.sort()
print(subject)

subject.reverse()
print(subject)

subject.pop()
subject.pop() #last item delete
print(subject)

subject2=subject.copy()  #item copy
print(subject2)  

pos=subject.index("java") #index number
print(pos)



subject.clear()
print(subject)


