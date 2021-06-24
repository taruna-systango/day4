import os

#give current directory
#print(os.getcwd())

#craete new directory
#os.mkdir('new-mydir')

#craete new child-directory in parent directory
#in parent not exist then error occur
#os.mkdir('new-mydir/child-mydir')

#if you want to create parent and child both
#os.makedirs('parent-dir/child-dir/grand-child-dir')

'''
#change directory
os.chdir('new-mydir')
print(os.getcwd())
'''

#rename directory
#os.rename('new-mydir','yourdir')

''''
#os.chdir('parent-dir')
os.chdir('child-dir')
print(os.getcwd())
os.rmdir('grand-child-dir')
'''
#remove inner directory
#os.chdir('yourdir')
#print(os.getcwd())
#os.rmdir('yourdir/child-mydir')

#remove all 
#os.removedirs('parent/child-dir')

'''
#walk
w = os.walk('.')
for i in w:
    print(i)
'''
#specific directory
w = os.walk('parent-dir')
for i in w:
    print(i)

#specific directory buttom-to-top
w = os.walk('parent-dir', topdown=False)
print(" buttom-to-top")
for i in w:
    print(i)

