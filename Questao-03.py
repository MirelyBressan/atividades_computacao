#Saída do nome do desenvolvedor:

print("Bem-vindos a Madereira da Mirely Bressan!")

#Escolha do tipo de madeira:

def escolha_tipo():
  while True:
    print("Escolha abaixo o tipo de madeira desejada:")
    print("Tora de Pinho    --(PIN)--")
    print("Tora de Peroba   --(PER)--")
    print("Tora de Mogno    --(MOG)--")
    print("Tora de Ipê      --(IPE)--")
    print("Tora de Imbuia   --(IMB)--")

    tipo = input("Informe o tipo de madeira desejada: ").upper()
    if tipo != "PIN" and tipo != "PER" and tipo != "MOG" and tipo != "IPE" and tipo != "IMB":
      print("")
      print("Tipo de madeira indisponível! Escolha outro tipo: ")
      continue
    else:
      print("")
      print("Tipo de madeira escolhido!")
      if tipo == "PIN":
        valor = 150.40
      elif tipo == "PER":
        valor = 170.20
      elif tipo == "MOG":
        valor = 190.90
      elif tipo == "IPE":
        valor = 210.10
      else:
       valor = 220.70
      return valor

#Informa o valor da quantidade desejada de madeira:

def qtd_toras():
  while True:
    try:
      print("")
      quantidade = float(input("Informe a quantidade de toras desejada em M³: "))
    except:
      print("")
      print("Valor inválido! Informe um valor numérico!")
      continue

    if quantidade < 100:
      desconto = 0
    elif quantidade < 500:
      desconto = 4/100
    elif quantidade < 1000:
      desconto = 9/100
    elif quantidade <= 2000:
      desconto = 16/100
    else:
      print("")
      print("Quantidades acima de 2000 M³ não são aceitas!")
      continue
    return quantidade, desconto

#Escolha do tipo de transporte:

def transporte():
  while True:
    print("")
    print("Escolha abaixo o tipo de transporte desejado:")
    print("Transporte Rodoviário    --(1)--    R$ 1.000,00")
    print("Transporte Ferroviário   --(2)--    R$ 2.000,00")
    print("Transporte Hidroviário   --(3)--    R$ 2.5000,00")

    print("")
    transporte = int(input("Informe o tipo de transporte desejado: "))
    if transporte != 1 and transporte != 2 and transporte != 3:
      print("")
      print("Tipo de transporte indisponível! Escolha o tipo disponível: ")
      continue
    else:
      print("")
      print("Transporte escolhido!")

      if transporte == 1:
        valor_transporte = 1000
      elif transporte == 2:
        valor_transporte = 2000
      else:
        valor_transporte = 2500

      return valor_transporte


tipo_madeira = escolha_tipo()
quantidade, desconto = qtd_toras()
valor_transporte = transporte()

#Calcula o valor do pedido:

total = ((tipo_madeira * quantidade)*(1-desconto)) + valor_transporte

#Saída final do valor total do pedido:

print("")
print(f"O valor final do pedido é de: R$ {total:.2f}")