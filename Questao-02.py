#Saída do nome do desenvolvedor e do menu:

print("--------- Sejam bem-vindos à Pizzaria da Mirely Bressan! ---------")
print("------------------------------------------------------------------")
print("------------------------------ Menu ------------------------------")
print(" Tamanho -- | -- Pizza Salgada -> (PS) -- | -- Pizza Doce -> (PD) ")
print("    P       |           R$ 30,00          |        R$ 34,00       ")
print("    M       |           R$ 45,00          |        R$ 48,00       ")
print("    G       |           R$ 60,00          |        R$ 66,00       ")

#Escolha dos sabores e tamanhos das pizzas:

valor_total = 0
while True:
  sabor = input("Gostaria de qual sabor de pizza? ").upper()
  if (sabor != "PS" and sabor != "PD"):
    print("Sabor indisponível! Escolha outro sabor: ")
    continue
  else:
      print("Sabor escolhido!")
  while True:
    print("")
    tamanho = input("Gostaria de qual tamanho de pizza? ").upper()
    if (tamanho != "P" and tamanho != "M" and tamanho != "G"):
      print("Tamanho indisponível! Escolha outro tamanho: ")
      continue
    else:
      print("Tamanho escolhido!")
      break

  if sabor =="PS":
    if tamanho == "P":
      valor = 30
    elif tamanho == "M":
      valor = 45
    else:
      valor = 60
  else:
    if tamanho == "P":
      valor = 34
    elif tamanho == "M":
      valor = 48
    else:
      valor = 66

#Saída do tamanho e sabor escolhido:

  print("")
  print(f"O  sabor escolhido foi {sabor}, no tamanho {tamanho}, fica no valor de R$ {valor:.2f}. ")
  print("")
  valor_total += valor

#Pergunta se deseja adicionar mais algum pedido:

  pergunta = input("Gostaria de adicinar mais algum sabor? (S ou N) ").upper()
  print("")
  if pergunta != "S":
    print("")
    print("Pedido finalizado!")
    break

#Saída do valor total final do pedido:

print("")
print(f"O valor total do pedido fica: R$ {valor_total:.2f}  ")