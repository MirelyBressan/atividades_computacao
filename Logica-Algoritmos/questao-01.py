#Saída do nome do desenvolvedor:

print("Bem-vindos ao sistema desenvolvido por Mirely Bressan!")

#Solicitação das informações de valor base e idade:

valor_base = float(input("Digite o valor base do plano em reais: R$ "))
idade = int(input("Digite a idade do cliente: "))

#Calculo das porcentagens de acordo com a idade:

if idade < 19:
  porcentagem = 100/100
elif idade  < 29:
  porcentagem = 150/100
elif idade < 39:
  porcentagem = 225/100
elif idade < 49:
  porcentagem = 240/100
elif idade < 59:
  porcentagem = 350/100
else:
  porcentagem = 600/100

#Calculo do valor mensal do plano:

valor_mensal = valor_base * porcentagem

#Saída do resultado do plano mensal:

print(f"O valor mensal do plano para a idade {idade} anos é de: R$ {valor_mensal:.2f}")