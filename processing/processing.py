import zipfile 
from os import scandir, rename, makedirs



if __name__ == "__main__":
    makedirs("extracted", exist_ok=True)
    files = (f for f in scandir("temp") if f.is_file())
    for ff in files:
        try:
            zi = zipfile.ZipFile("temp/"+ff.name)
        except:
            print(f"Invalid zip file - {ff.name}")
        else:
            zi.extractall("extracted")
        try: 
            rename(f"./extracted/aplic/sead/lista_filiados/uf/{ff.name.split('.')[0]}.csv", f"./extracted/{ff.name.split('.')[0]}.csv")
        except:
            print(f"Invalid zip - {ff.name}")