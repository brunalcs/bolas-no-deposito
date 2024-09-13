from math import ceil
c = float (input("Qual o comprimento do depósito? "))
l = float (input("Qual a largura do depósito? "))
a = float(input("Qual a altura do depósito? "))
volume_deposito = c*l*a
print("Digite alguma das opções abaixo")
print("Bola de Basquete Adulto\nBola de Basquete Infantil\nBola de Futebol Oficial\nBola de Vôlei\nBola de Handball\nBola de Futebol de Salão\nOutro tamanho de bola")
bola = (input())

if bola == "Bola de Basquete Adulto":
    volume_bba = 24**3
    print (f"A quantidade de bolas que cabem nesse depósito é {volume_deposito/volume_bba:.0f}")
elif bola == "Bola de Basquete Infantil":
    volume_bbi = 22**3
    print(f"A quantidade de bolas que cabem nesse depósito é {volume_deposito/volume_bbi:.0f}")
elif bola == "Bola de Futebol Oficial":
    volume_bfo = 22**3
    print(f"A quantidade de bolas que cabem nesse depósito é {volume_deposito/volume_bfo:.0f}")
elif bola == "Bola de Vôlei":
    volume_bv = 21**3
    print(f"A quantidade de bolas que cabem nesse depósito é {volume_deposito/volume_bv:.0f}")
elif bola == "Bola de Handball":
    volume_hd = 19**3
    print(f"A quantidade de bolas que cabem nesse depósito é {volume_deposito/volume_hd:.0f}")
elif bola == "Bola de Futebol de Salão":
    volume_bfs = 20**3
    print(f"A quantidade de bolas que cabem nesse depósito é {volume_deposito/volume_bfs:.0f}")
elif bola == "Outro tamanho de bola":
    novo_tamanho = float(input("Digite um tamanho:"))
    volume_nt = novo_tamanho**3
    print(f"A quantidade de bolas que cabem nesse depósito é {volume_deposito/volume_nt:.0f}")
else:
    print("Selecione alguma das opções acima")




