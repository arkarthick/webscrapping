from os import listdir

path = "C:\\Users\\dARK_soul\\Desktop\\Git\\srenterprise\\images"
files = listdir(path)
li = []
a = [806]
for i in files:
	x = i[:-4]
	li.append(int(x))

print(set(li+a))
