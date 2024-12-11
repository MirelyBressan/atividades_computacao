#Saída do nome do desenvolvedor e do menu:

print("--------- Sejam bem-vindos a Lista de Contatos da Mirely Bressan! ---------")

lista_contatos = []
id_global = 4319609

#Cadastro dos contatos:

def cadastrar_contato(id):
  print("")
  print("------------------------------------------------------------------")
  print("---------------------- Cadastrar Contato -------------------------")
  print(f"O Id do contato é: {id}")
  nome = input("Informe o nome do contato: ")
  atividade = input("Informe a atividade do contato: ")
  telefone = int(input("Informe o telefone do contato: "))

  dic_contato = {'Id': id, 'Nome': nome, 'Atividade': atividade, 'Telefone': telefone}
  lista_contatos.append(dic_contato.copy())

#Consulta dos contatos:

def consultar_contato():
  print("")
  print("------------------------------------------------------------------")
  print("---------------------- Consultar Contato -------------------------")
  print("---- Consultar todos os contatos ---(1)--- ")
  print("---- Consultar por ID            ---(2)--- ")
  print("---- Consultar por Atividade     ---(3)--- ")
  print("---- Retornar ao menu principal  ---(4)--- ")

  while True:
      print("")
      opcao = int(input("Informe a opção desejada: "))
      if opcao == 1:
        for contato in lista_contatos:
          for chave in contato:
            print(f"{chave}: {contato[chave]}")
          print("")
      elif opcao == 2:
        id_consulta = int(input("Informe o ID do contato que deseja consultar: "))
        for contato in lista_contatos:
          if contato['Id'] == id_consulta:
            for chave in contato:
              print(f"{chave}: {contato[chave]}")
      elif opcao == 3:
        atividade_consulta = input("Informe a atividade do contato que deseja consultar: ")
        for contato in lista_contatos:
          if contato['Atividade'] == atividade_consulta:
            for chave in contato:
              print(f"{chave}: {contato[chave]}")
      elif opcao == 4:
        return
      else:
        print("Opção inválida! Escolha uma opção válida!")

#Remoção dos contatos:

def remover_contato():
  while True:
    print("")
    print("------------------------------------------------------------------")
    print("----------------------- Remover Contato --------------------------")
    id_consulta = int(input("Informe o ID do contato que deseja remover: "))
    for contato in lista_contatos:
      if contato['Id'] == id_consulta:
        lista_contatos.remove(contato)
        print("")
        print("Contato removido com sucesso!")
        return
    print("")
    print("Contato não encontrado!")

#Menu principal com as opções disponíveis:

while True:
  print("")
  print("------------------------------------------------------------------")
  print("------------------------ Menu Principal- -------------------------")
  print("---- Cadastrar Contato            ---(1)--- ")
  print("---- Consultar Contatos           ---(2)--- ")
  print("---- Remover Contato              ---(3)--- ")
  print("---- Sair                         ---(4)--- ")

  opcao = int(input("Informe a opção desejada: "))
  if opcao == 1:
    id_global += 1
    cadastrar_contato(id_global)
  elif opcao == 2:
    consultar_contato()
  elif opcao == 3:
    remover_contato()
  elif opcao == 4:
    break
  else:
    print("Opção inválida! Escolha uma opção válida!")