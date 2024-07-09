import cv2
import pytesseract as pt 

caminho = r"C:\Program Files\Tesseract-OCR"
pt.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'

img = cv2.imread("icaro.jpg")

#print(pt.pytesseract.image_to_string(img, lang="por"))
boxes = pt.pytesseract.image_to_boxes(img, lang="por")
dados = pt.pytesseract.image_to_data(img, lang="por")

print(dados)
img_h, img_w, _ = img.shape

"""
for b in boxes.splitlines():
    b = b.split(" ")
    #print(b)
    letra, x, y, w, h = b[0], int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img,(x,img_h-y),(w,img_h-h),(0,0,255),1)
    cv2.putText(img, letra, (x, img_h-y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

   """
   
for x,linha in enumerate(dados.splitlines()):
    
    if x!=0:
        
        linha = linha.split()
        print(linha)
        
        if len(linha) == 12:
            x, y, w, h = int(linha[6]), int(linha[7]), int(linha[8]), int(linha[9])
            palavra = linha[11]
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            cv2.putText(img, palavra, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
  
   
cv2.imshow("Imagem", img)


cv2.waitKey(0)
cv2.destroyAllWindows()