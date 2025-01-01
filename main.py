import os 

currentDir = os.getcwd() # Get the current working Directory
mainFile = os.path.join(currentDir , 'main.py') # Get the path to this file so it does not get altered
os.chmod(mainFile , 0o777) # Set the read and write permission for this file
files = os.listdir(currentDir) # Get the list of all the files in the current folder
files.remove('main.py') # Remove this file from the list of files


extensionFolderNames = {
    'txt': 'Text Files',
    'py': 'Python Files',
    'cpp': 'C++ Programms',
    'xlsx': 'Excel Sheets',
    'pptx': 'PowerPoint Presentations',
    'go': 'GoLang',
    'java': 'Java'
}

for i in files:
    os.makedirs(extensionFolderNames[i.split('.')[1]]) # Make a folder according to the extenison of current file in the loop
    source = os.path.join(currentDir , i) # Path of current file in the loop
    destin = os.path.join(currentDir , extensionFolderNames[i.split('.')[1]] , i) # Destionation path
    os.replace(source , destin) # Move the source file to desination

