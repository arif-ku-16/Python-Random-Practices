import os
files = os.listdir()
files.remove('1main.py')
def createFolderIfNot(folder):
    if(not os.path.exists(folder)):
        os.makedirs(folder)
createFolderIfNot("Images")
createFolderIfNot("Pdf Files")
createFolderIfNot("Latex Files")
createFolderIfNot("Other Items")

imgExtensions=['.png','.PNG','.jpg']
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExtensions]
pdfExtensions=['.pdf']
pdfiles=[]
for file in files:
    if(os.path.splitext(file)[1].lower() in pdfExtensions):
        pdfiles.append(file)
texExtensions=['.tex', '.txt']
latex=[file for file in files if os.path.splitext(file)[1]in texExtensions]

others=[]
for file in files:
    file2=os.path.splitext(file)[1].lower()
    if(file2 not in imgExtensions) and (file2 not in pdfExtensions) and (file2 not in texExtensions) and os.path.isfile(file):
        others.append(file)

def replace(folderName, fileNames):
    for item in fileNames:
        os.replace(item,f"{folderName}/{item}")

replace("Images",images)
replace("Pdf Files", pdfiles)
replace("Latex Files",latex)
replace("Other Items", others)
