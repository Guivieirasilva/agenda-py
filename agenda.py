print("Agenda")

agenda = []


def addContact(
    agenda: list, nameContact: str, phone: str, email: str, isFavorite=False
):
    contact = {
        "name": nameContact,
        "phone": phone,
        "email": email,
        "isFavorite": isFavorite,
    }
    agenda.append(contact)

    print(f"Contato do '{nameContact}' foi cadastrado com sucesso!")
    print(agenda)
    return


def viewListContacts(agenda: list):
    print("\nLista de contatos: ")
    for index, contact in enumerate(agenda, start=1):
        favorite = "✔" if contact["isFavorite"] else " "
        nameContact = contact["name"]
        phoneContact = contact["phone"]
        emailContact = contact["email"]
        print(
            f"\n{index} - {nameContact} |",
            f"{emailContact} - {phoneContact} - [{favorite}]",
        )
    return


def editContact(agenda: list, index: int):

    numberContact = index - 1

    if numberContact >= 0:

        name = input("Digite o nome do contato: ")
        phone = input("Digite o número de telefone: ")
        email = input("Digite o seu e-mail: ")

        agenda[numberContact] = {
            "name": name,
            "phone": phone,
            "email": email,
            "isFavorite": False,
        }

        print(
            f"\nO Contato '{agenda[numberContact]["name"]}'",
            "foi atualizado com sucesso!",
        )

    else:

        print(f"\nO contato de número: {numberContact} não existe!")
        print(agenda)

    return


def changeContacts(agenda: list, index: int):
    numberContact = index - 1

    if numberContact >= 0:
        contact = agenda[numberContact]
        contact["isFavorite"] = not contact["isFavorite"]

        if contact["isFavorite"]:
            print(f"\n {contact["name"]} foi adicionado aos favoritos!")
        else:
            print(f"\n {contact["name"]} foi removido dos favoritos!")
    else:
        print("\n Contato não encontrado.")


def viewListContactsFavorites(agenda: list):
    print("\n Lista de contatos favoritos: ")

    favoritos = list(filter(lambda c: c.get("isFavorite", False), agenda))

    if not favoritos:
        print("\n Nenhum contato favorito encontrado.")
        return

    for index, contact in enumerate(favoritos, start=1):
        nameContact = contact["name"]
        phoneContact = contact["phone"]
        emailContact = contact["email"]

        print(
            f"\n{index} - {nameContact} |",
            f"{emailContact} - {phoneContact} - [✔]",
        )


def deletedContact(agenda: list, index: int):
    numberContact = index - 1

    if numberContact >= 0:
        contact = agenda[numberContact]
        agenda.remove(contact)

        print(f"\n {contact["name"]} foi excluído!")

    else:
        print("\n Contato não encontrado.")


def exitAgenda():
    print("\n Encerrando o programa. Até logo!")
    exit()


while True:

    print("\n====== AGENDA DE CONTATOS ======")
    print("1 - 📥 Adicionar um novo contato")
    print("2 - 📋 Visualizar todos os contatos salvos")
    print("3 - ✏️ Editar as informações de um contato existente")
    print("4 - ⭐ Marcar ou desmarcar um contato como favorito")
    print("5 - 🧡 Listar apenas os contatos favoritos")
    print("6 - 🗑️ Apagar um contato da agenda")
    print("0 - ❌ Sair do programa")

    select = int(input("\n Digite o número da função que deseja realizar: "))

    if select == 1:
        nameContact = input("Digite o nome do contato: ")
        phoneContact = input("Digite o número de telefone: ")
        emailContact = input("Digite o seu e-mail: ")

        addContact(agenda, nameContact, phoneContact, emailContact, False)

    elif select == 2:
        viewListContacts(agenda)

    elif select == 3:
        viewListContacts(agenda)

        index = int(input("Selecione o contato que deseja editar: "))

        editContact(agenda, index)

    elif select == 4:
        viewListContacts(agenda)

        index = int(input("Selecione o contato que deseja favoritar: "))

        changeContacts(agenda, index)

    elif select == 5:
        viewListContactsFavorites(agenda)

    elif select == 6:
        viewListContacts(agenda)

        index = int(input("Selecione o contato que deseja excluir: "))

        deletedContact(agenda, index)

    elif select == 0:
        exitAgenda()
