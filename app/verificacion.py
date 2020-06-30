import os.path

if os.path.isdir("C:/Users/Keymera/test/"):
    print('La carpeta existe.')
    if os.path.isfile("C:/Users/Keymera/test/filename.txt"):
        print('El archivo existe.')
    else:
        print('El no archivo existe.')
else:
    print('La carpeta no existe.')
