n = int(input())
student_marks = {}
value=0
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for i in student_marks[query_name]:
    value +=i
    avg = value / len(student_marks[query_name])

print("%.2f" %avg)
