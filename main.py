# init du liste pour stocker l'ensemble du prigramme
orange_center = []


# Fonction du menu pour demander à l'utlisateur de taper USSD d'orange money
def menuUSSD():
    ussdNumber = "#144#"

    while True:
        ask_user_to_enter_ussd = input("Veuillez taper ussd d'orange money: ")
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

#Fonction du sous menu de solde de mes comptes
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

            case _:
                print("Choix incorrect !")

#Fonction du sous menu qui concerne l'achat du crédit
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
            choix: """
        )

        match choix:
            case "1":
                credit()

            case "2":
                print("Pass")

            case "0":
                my_account()
                
            case "9":
                orange_money_menu()
                break

            case _:
                print("Choix incorrect !")

#Fonction du transfert d'argent
def transfer():
    print("Transfert d'argent")

#Fonction pour afficher le solde 
def solde():
    print("*********Solde de mes comptes:*********")
    my_solde = 100000
    print(f"Le solde de votre compte est de: {my_solde} FCFA")
    while True:
        back_interface = input("0:prec\n 9.Accueil ")
        # home_interface = input("9: Accueil")

        if back_interface == "0":
            my_account()
            break
        elif back_interface == "9":
             orange_money_menu()
        else:
            print("Choix incorrect !")

def credit():
    print("Crédit")

if __name__ == "__main__":
    menuUSSD()
