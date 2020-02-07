import os.path
import csv

images = os.scandir(os.getcwd() + "")# "/images")
#print(images)
sortedimages = sorted(images, key=lambda x: x.stat().st_mtime, reverse=False)
newlist = []

# Read the tsv
def readTsv():
	with open("Adjectives_Sample.tsv") as fd:
		rd = csv.reader(fd, delimiter="\t")
		for row in rd:
			print(row[3])

names = ['one.png', 'two.png', 'three.png']
def renameImages(names):
	index = 0
	for i in sortedimages:
		print(i.name)
	
		if(i.name.endswith(".png")):
			#print(i.stat().st_ctime)
			print(i.stat())
			print(i.name)
			print(names[index])
	#		os.rename("" + i.name, "" + names[index])
			index = index + 1
			
readTsv()
renameImages(names)
