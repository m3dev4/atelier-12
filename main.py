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
                1. Solde de mes comptes\n
                2. Achats: Crédit et Pass
                3. Transfert d'argent
                5. Quitter
                """
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
                1. Solde de mes comptes\n
                2. Achats: Crédit et Pass
                3. Transfert d'argent
                5. Quitter
                """
                )


def my_account():
    print("Solde de mes comptes")


def buying():
    print("Achats: Crédit et Pass")


def transfer():
    print("Transfert d'argent")

#Cette fonction a pour role de faire un retour à l'arriere l'endroit ou on etait
def navigation_back():
    back = 0
    while True:
        back_interface = input("Précedent 0: ")

        if back_interface == "0":
            orange_money_menu()
            break
        else:
            print("Choix incorrect !")
            
            
            
            
if __name__ == "__main__":
    menuUSSD()
