nome = input("Qual seu nome: ")
despesa1 = float(input("Digite a primeira despesa: "))
despesa2 = float(input("Digite a segunda despesa: "))
despesa3 = float(input("Digite a terceira despesa: "))

soma = despesa1 + despesa2 + despesa3
media = soma / 3

print("Olá,", nome, "!")
print("A soma das despesas é:", soma)
print("A média das despesas é:", media)