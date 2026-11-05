rutas = ["Maçã", "Banana", "Laranja", "Pêra"]
peca = input('Introduza o nome de uma fruta.').strip().capitalize()
if peca not in frutas:
    print ('Fruta não encontrada.')
else:
    print (f'A fruta {peca} está na lista!')