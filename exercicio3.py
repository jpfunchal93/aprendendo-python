frutas = ["Maçã", "Banana", "Laranja", "Pêra"]
pedido = input('Introduza o nome de uma fruta.').strip().capitalize()
if pedido not in frutas:
    print ('Fruta não encontrada.')
else:
    print (f'A fruta {pedido} está na lista!')