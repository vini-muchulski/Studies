import pytesseract
import cv2

# links uteis:
## https://www.youtube.com/watch?v=Wx3SyNwZtsA
# corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# instalar outra língua: https://github.com/tesseract-ocr/tessdata
# pegar linguas: print(pytesseract.get_languages())

# passo 1; carregar a imagem

imagem = cv2.imread("icaro.jpg")


# passo 2; pedir para o tesseract extrair o texto da imagem
# C:\Program Files\Tesseract-OCR

#r antes da string caminho indica que a string é uma string bruta. 
#Isso significa que o Python não interpretará caracteres especiais na string, como barras invertidas ou caracteres de escape.
caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'

texto = pytesseract.image_to_string(imagem,lang="por")
print(texto)

