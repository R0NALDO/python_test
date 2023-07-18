import os
#navega(caminha) e mostra os arquivos e pastas de um diretorio 

diretorio = "c:\ron" # "." dir atual 

def listar():
    for root, dirs, files in os.walk(diretorio, topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


listar()