import os.path
import shutil
import csv


images = os.scandir(os.getcwd() + "/Adjectives")
#print(images)
sortedimages = sorted(images, key=lambda x: x.stat().st_mtime, reverse=False)
newlist = []

# Read the tsv
def readTsv():
	result = []
	with open("deck.tsv", encoding='utf-8') as fd:
		rd = csv.reader(fd, delimiter="\t")
		
		for row in rd:
#			print(row[3])
			result.append(row[3])
	return result[1:]

names = ['one.png', 'two.png', 'three.png']
def renameImages(names):
	index = 0
	print(len(sortedimages))
	for i in sortedimages:
		if(True or i.name.endswith(".jpeg")):
			#print(i.stat().st_ctime)
			#print(i.stat())
			extension = ""
			if(i.name.endswith(".png")):
				extension = ".png"
			print(i.name)
			print(names[index])
			dir = "Adjectives/"
#			os.rename("images/" + i.name, "images/" + names[index])
			shutil.copyfile(dir + i.name, "test1/" + names[index] + extension)
			index = index + 1
			
test = readTsv()
#print(test)
renameImages(test)
