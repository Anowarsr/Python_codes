from sys import argv

script,User_name = argv
promt = '>'

print(f"Hi{User_name}.I'm good in {script}")
print(f"You Know my name!{User_name}")

tags = input(promt)

print("Which type of laptop you have?")
laptop = input(promt)
print("Where is your Hometown?")
hometown = input(promt)

print(f'''okay, you said {tags} knowabout me, 
currently yo hava {laptop} laptop 
and you said me your hometown is {hometown}.
thanks to talking me Great Day''')