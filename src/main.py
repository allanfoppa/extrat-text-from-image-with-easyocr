import easyocr

reader = easyocr.Reader(['pt'])

results = reader.readtext(
  'src/assets/coach_de_fracassos_frase_1.jpg',
  paragraph=False
)

for result in results:
  print(
    f'Texto: {result[0]}\n'
    f'Posição: {result[1]}\n'
  )