from sys import argv

print("Enter filename : ")
filename=input("Enter:")

print(f"we are going to create{filename}.")
print("if you dont want that,hit return")

input("?")

print("opening the file ......")
target=open(filename,'w')
print("truncTING THE FILE.GOODBYE!")
# target.truncate()
print("Now i'm going to ask some lines in yoyr file: ")

line1= input("line 1: ")
line2= input("line 2: ")
line3= input("line 3: ")

print(" i'm going to write this to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("We are done")
target.close()

# 
print("your written text file here,")
txt=open(filename)
print(txt.read())
txt.close()