#Saída nome do desenvolvedor:

print("Bem vindo ao Sistema da Mirely Bressan!")

#Receber os valores do plano e idade:

valorBase = float(input("Informe o valor base do plano: R$ "))
idade = int(input("Informe a idade do cliente: "))

#Calculo da porcentagem de acordo com a idade:

if 0 <=idade< 19:
    porcentagem = 100/100
elif 19 <=idade<29:
    porcentagem = 150/100
elif 29 <=idade< 39:
    porcentagem = 225/100
elif 39 <=idade< 49:
    porcentagem = 240/100
elif 49 <=idade< 59:
    porcentagem = 350/100
else:
    porcentagem = 600/100

valorMensal = valorBase * porcentagem

print(f"O valor do Plano Mensal para {idade} anos é: R$ {valorMensal:.2f}")