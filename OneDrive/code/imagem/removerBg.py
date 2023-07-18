#remove o fundo de uma imagem, funcionou perfeitamente
from rembg import remove
from PIL import Image

def removerFundo(caminho_imagem): #caminho da imagem

    img = Image.open(caminho_imagem)
    imgRemove = remove(img)
    imgRemove.save(r"c:\Users\ronal\Pictures\semFundo\imagem_sem_fundo.png")


removerFundo(r"c:\Users\ronal\OneDrive\imagem\saveiro_bola.webp")