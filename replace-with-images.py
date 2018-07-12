#from xml.dom import minidom
import sys, re

# for arg in sys.argv:
#  	print 'arg:', arg


inName = sys.argv[1]
folderName = ''
outName = 'output'

print len(sys.argv)

if len(sys.argv) == 3:
	folderName = sys.argv[2]
if len(sys.argv) == 4:
	outName = sys.argv[3]
print inName

#doc = minidom.parse(inName)

#itemlist = xmldoc.getElementsByTagName('item')

from bs4 import BeautifulSoup

formats = ['jpg', 'jpeg', 'png', 'gif']

soup = BeautifulSoup(open(inName), "xml")

labels = soup.find('g', {'id' : 'node-labels'})

texts = labels.find_all('text')

#print labels

for text in texts:
	x = float(text['x'])
	y = float(text['y'])
	size = float(text['font-size'])
	name = text.get_text()
	match = re.findall(r"(?=([^ \n].+\."+'|'.join(formats)+r"))", name)

	if len(match)>0:
		new_tag = soup.new_tag("image", x=x - size/2,y=y - size/2, width=size, height=size)
		new_tag['xlink:href'] = folderName + "/" + match[0]
		print new_tag
		text.replace_with(new_tag)

with open(outName+".svg", "w") as file:
    file.write(str(soup))
