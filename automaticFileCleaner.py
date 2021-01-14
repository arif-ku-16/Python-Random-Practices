import os
files= os.listdir()
files.remove('1main.py')
#print(files)
def createIfNotExist(fName):
    if(not os.path.exists(fName)):
        os.makedirs(fName)
createIfNotExist("Images")
createIfNotExist("TexFile")
createIfNotExist("Media")
imgExtns=['.png', '.jpg']
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExtns]
#print(images)
docExtns=['.tex']
Docxx=[file for file in files if os.path.splitext(file)[1] =='.tex']
#print(Docxx)
Media=[]
for file in files:
    if (os.path.splitext(file)[1].lower() not in imgExtns) and(os.path.splitext(file)[1].lower() not in docExtns) and os.path.isfile(file):
        Media.append(file)
print(Media)
for img in images:
    os.replace(img,f"Images/{img}")
for tx in Docxx:
    os.replace(tx,f"TexFile/{tx}")
