import sys, re
from bs4 import BeautifulSoup

inName = sys.argv[1]
folderName = ''
upscale = 1.0
outName = 'output'

if len(sys.argv) > 2:
	folderName = sys.argv[2]
if len(sys.argv) > 3:
	upscale = float(sys.argv[3])
if len(sys.argv) > 4:
	outName = sys.argv[4]

formats = ['jpg', 'jpeg', 'png', 'gif']

soup = BeautifulSoup(open(inName), "xml")
labels = soup.find('g', {'id' : 'node-labels'})
texts = labels.find_all('text')

newLabels = soup.new_tag("g", id="newgroups")
imgTags = soup.new_tag("g", id="images")
textTags = soup.new_tag("g", id="labels")

newLabels.append(imgTags)
newLabels.append(textTags)

for text in texts:
	x = float(text['x'])
	y = float(text['y'])
	size = float(text['font-size']) * upscale
	name = text.get_text()
	match = re.findall(r"([^ \n].+\.("+'|'.join(formats)+"))", name, re.IGNORECASE)

	if len(match)>0:
		new_tag = soup.new_tag("image", x=x - size/2,y=y - size/2, width=size, height=size)
		new_tag['xlink:href'] = folderName + match[0][0]
		print new_tag
		imgTags.append(new_tag)
	else:
		textTags.append(text)

labels.replace_with(newLabels)

with open(outName+".svg", "w") as file:
	file.write(str(soup))
