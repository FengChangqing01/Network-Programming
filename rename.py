import os,re,shutil
import PyPDF2

path = r"C:\Users\fWX589413\Desktop\test\test"

def rename_PDF():
    """"get names of files"""
    files = os.listdir(path)
    print(files)

    """make foler to save renamed files"""
    newFoler = os.path.join(path, 'rename')
    if os.path.exists(newFoler) == True:
        shutil.rmtree(newFoler)
    os.makedirs(newFoler)

    """rename files which match regex"""
    regex = re.compile(r'(\()(\d\d)(\))')
    for file in files:
        mo = regex.search(file)
        if mo != None:
            newName = "偷偷第"+mo.group(2)+'话.pdf'
            print("Rename file: "+file+"---->"+newName+".....")
            shutil.copy(os.path.join(path,file), os.path.join(newFoler,newName))


if __name__ == "__main__":
    rename_PDF()