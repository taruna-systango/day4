from google.colab import files
uploaded = files.upload()
for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
uploaded

#create new file
f = open("myfile.txt", "x")
#f = open("myfile.txt", "w")

1#create new file
f = open("myfile1.txt", "w")
f.write("this is myfile")
f.close()
p = open("myfile1.txt","r")
print(p.read())
f.close()

import os
os.remove("myfile.txt")

#f = open("day4file.txt", "r")
#print(f.read())
#print(f.readline())
#print(f.read(5))

f = open("day4file.txt", "a")
f.write(" i am student of MCA. ")
f.close()
f = open("day4file.txt", "r")
#print(f.read())
print(f.readline())