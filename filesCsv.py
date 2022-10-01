"""
'r'(read)=opens the file for reading the file .its started beginning of the file
'r+'(read+write) =open files both reading and writing. started beginning
'w'(write)= open the file for writing. create one if those file dosenot exist. started beginning
'w+'(writing+reading) =open the file for reading or writing , started beginning. create file if does not exist.
'a' (appending) =similar to 'w' but started end
'a+'(writing+reading)= similar to w+ but started end.
"""
"""
f=open('a.text','w');
#getting info

print('name=',f.name);  #file name
print('is it closed? ', f.closed) #file open or closed
print('Mode =',f.mode) #file mode
f.write("python is my fav language") #file write
f.close()  #file close

#append
f = open('a.text','a')
f.write("i also love java")
f.close();
#r+
f =open('a.text', 'r+')
info=f.read(12);
print(info);
f.close();
#w
f=open('a.text', 'w+')
f.write("all clear")
f.close()
"""
import csv
#csv file read
file=open('example.csv')
file_reader=csv.reader(file)

#data =list(file_reader)
#print(data)
#print('list checking',data[1][0])
for row in file_reader:
     print('Row no='+str(file_reader.line_num)+''+str(row))

output_file = open ('out.csv','w',newline='')
output_writer= csv.writer(output_file,delimiter ='.')
output_writer.writerow(['1','2','3','4'])
output_writer.writerow(['15','16','20'])
output_file.close()
