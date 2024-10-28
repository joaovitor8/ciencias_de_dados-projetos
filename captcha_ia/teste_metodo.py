import cv2
from PIL import Image

# 0 - Testando metodos para ver qual é o melhor para o tratamento das imagens

metodos = [
  cv2.THRESH_BINARY,
  cv2.THRESH_BINARY_INV,
  cv2.THRESH_TRUNC,
  cv2.THRESH_TOZERO,
  cv2.THRESH_TOZERO_INV
]

imagem = cv2.imread("bd_captcha/telanova8.png")


imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

i = 0
for metodo in metodos:
  i += 1
  _, imagem_tratada = cv2.threshold(imagem_cinza, 127, 255, metodo or cv2.THRESH_OTSU)
  cv2.imwrite(f'testes_metodo/imagem_tratada_{i}.png', imagem_tratada)


imagem = Image.open('testes_metodo/imagem_tratada_3.png')
imagem = imagem.convert("P")
imagem2 = Image.new("P", imagem.size, (255, 255, 255))

for x in range(imagem.size[1]):
  for y in range(imagem.size[0]):
    cor_pixel = imagem.getpixel((y, x))
    if cor_pixel < 115:
      imagem2.putpixel((y, x), (0, 0, 0))

imagem2.save('testes_metodo/imagemfinal.png')
