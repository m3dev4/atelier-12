# init du liste pour stocker l'ensemble du prigramme
orange_center = [{"balance": 100000}]

code_secret = 45254


# Fonction du menu pour demander à l'utlisateur de taper USSD d'orange money
def menuUSSD():
    ussdNumber = "#144#"

    while True:
        ask_user_to_enter_ussd = input()
        if ask_user_to_enter_ussd == ussdNumber:
            orange_money_menu()
            break

        else:
            print("USSD incorrecte ! Mettez la bonne ussd: ")


# Fonction du menu Orange Menu
def orange_money_menu():
    print(
        """
        )  (               )                *       )     )         )  
        ( /(  )\ )   (     ( /( (            (  `   ( /(  ( /(      ( /(  
        )\())(()/(   )\    )\()))\ )   (     )\))(  )\()) )\())(    )\()) 
        ((_)\  /(_)|(((_)( ((_)\(()/(   )\   ((_)()\((_)\ ((_)\ )\  ((_)\  
        ((_)(_))  )\ _ )\ _((_)/(_))_((_)  (_()((_) ((_) _((_|(_)__ ((_) 
        / _ \| _ \ (_)_\(_) \| (_)) __| __| |  \/  |/ _ \| \| | __\ \ / / 
        | (_) |   /  / _ \ | .` | | (_ | _|  | |\/| | (_) | .` | _| \ V /  
        \___/|_|_\ /_/ \_\|_|\_|  \___|___| |_|  |_|\___/|_|\_|___| |_|   
                                                                        
        """
    )

    while True:
        choix = input(
            """
        1. Solde de mes comptes
        2. Achats: Crédit et Pass
        3. Transfert d'argent
        5. Quitter
        choix: """
        )

        match choix:
            case "1":
                my_account()

            case "2":
                buying()

            case "3":
                transfer()

            case "5":
                print("Au revoir")
                break

            case _:
                print("Choix incorrect !")
                choix = input(
                    """
                1. Solde de mes comptes
                2. Achats: Crédit et Pass
                3. Transfert d'argent
                5. Quitter
                choix: """
                )
                continue
        break


# Fonction du sous menu de solde de mes comptes
def my_account():
    print("*********Mon compte:*********")
    while True:
        choix = input(
            """
            1. Solde du compte
            2. Mon salaire
              --- 
            0. prec
            9. Accueil
            8. Quitter
            choix: """
        )

        match choix:
            case "1":
                solde()

            case "2":
                print("Mon salaire")

            case "0" | "9":
                orange_money_menu()
                break
            case "8":
                print("Au revoir")
                break

            case _:
                print("Choix incorrect !")


# Fonction du sous menu qui concerne l'achat du crédit
def buying():
    print("*********Achats: Crédit et Pass*********")
    while True:
        choix = input(
            """
            1. Crédit
            2. Pass
              --- 
            0. prec
            9. Accueil
            8. Quitter
            choix: """
        )

        match choix:
            case "1":
                credit()

            case "2":
                menu_forfait()

            case "0" | "9":
                orange_money_menu()
                break
            case "8":
                print("Au revoir")
                break

            case _:
                print("Choix incorrect !")


# Fonction du transfert d'argent
def transfer():
    print("*************Transfert d'argent*************")

    while True:
        choix = input(
            """
            1. Envoyer en local
            2. Envoyer international
              --- 
            0. prec
            9. Accueil
            8. Quitter
            choix: """
        )

        match choix:
            case "1":
                send_money_local()

            case "2":
                print("Pass")

            case "0" | "9":
                orange_money_menu()
                break
            case "8":
                print("Au revoir")
                break

            case _:
                print("Choix incorrect !")


# Fonction pour afficher le solde
def solde():
    print("*********Solde de mes comptes:*********")

    for i in orange_center:
        my_solde = i["balance"]
        print(f"Votre solde est de {my_solde} FCFA")
    while True:
        back_interface = input("0:prec\n 9.Accueil ")

        if back_interface == "0":
            my_account()
            break
        elif back_interface == "9":
            orange_money_menu()
        else:
            print("Choix incorrect !")
    return my_solde


# fonction pour acheter du credit
def credit():

    while True:
        for i in orange_center:
            my_solde = i["balance"]
        try:
            montant = int(input("Veuillez entrer le montant du crédit: "))

            if montant < 0:
                print("Le montant ne peut pas être négatif")
                continue
            elif montant > my_solde:
                print("Le montant ne peut pas être supérieur au solde")
                continue
            else:
                break

        except ValueError:
            print("Veuillez entrer un nombre entier")
            continue

    new_solde = my_solde - montant
    i["balance"] = new_solde
    i["credit"] = montant
    print(i)

    print(
        f"L'achat du crédit a été effectuer avec succes. Votre solde est de {new_solde} FCFA."
    )


def menu_forfait():
    print("*********Achat de forfait:*********")
    while True:
        menu_forfait = """
        1. Pass 100 Mo - 500fcfa
        2. Pass 500 Mo - 1000fcfa
        3. Pass 1 Go - 2000fcfa
        --
        0. prec
        9. Accueil
        8. Quitter
    """
        print(menu_forfait)
        choix = input("Veuillez choisir un forfait: ")
        match choix:
            case "1":
                acheter_forfait(500)
            case "2":
                acheter_forfait(1000)
            case "3":
                acheter_forfait(2000)
            case "9":
                orange_money_menu()
            case "0":
                buying()
            case "8":
                print("Au revoir")
                break
            case _:
                print("Choix incorrect !")


def acheter_forfait(prix):
    message = (
        "Vous êtes sur le point d'acheter un forfait à "
        + str(prix)
        + "FCFA. \n1. Confirmer \n2. Annuler\nchoix:"
    )
    for i in orange_center:
        my_solde = i["balance"]

        if prix > my_solde:
            print("Le montant ne peut pas être supérieur au solde")
        elif prix < 0:
            print("Le montant ne peut pas être négatif")
        else:
            if input(message) == "1":
                while True:
                    try:
                        input_code = int(input("Veuillez entrer votre code secret: "))
                        if input_code == code_secret:
                            new_solde = my_solde - prix
                            i["balance"] = new_solde
                            i["forfait"] = prix
                            print(i)
                            print(
                                f"L'achat du forfait a été effectuer avec succes. Votre solde est de {new_solde} FCFA."
                            )
                            return
                        else:
                            print("Code incorrect ! Veuillez réessayer.")
                    except ValueError:
                        print("Veuillez entrer un nombre entier")
                        continue


# fonction pour transferer de l'argent en local
def send_money_local():
    print("*********Transfert d'argent en local*********")
    while True:
        for i in orange_center:
            my_solde = i["balance"]
        try:
            montant = int(
                input("Veuillez saisir le montant que vous souhaitez envoyer: ")
            )
            numero = input("Veuillez saisir le numéro du déstinataire: ")

            if montant < 0:
                print("Le montant ne doit pas être négatif")
                continue
            elif montant > my_solde:
                print("Le montant ne doit être pas superieur")
                continue
            elif len(numero) != 9:
                print("Le numéro doit contenir 9 chiffre")
            else:
                break

        except ValueError:
            print("Veuillez entrer un nombre entier")
            continue

    new_solde = my_solde - montant
    i["balance"] = new_solde
    i["transfert_destinataire"] = montant
    print(i)
    print(
        f"Le transfert vers le numero {numero} a été effectué avec succes. Votre solde est de {new_solde} FCFA."
    )


if __name__ == "__main__":
    menuUSSD()
