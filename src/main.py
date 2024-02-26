import time
import json
import os


def attack():
    # currPath = os.getcwd()
    # print("Current path: ", currPath)

    # TODO: verify if this path will chagne when the app is deployed
    with open('src/db.json', 'r') as db:
        data = json.load(db)
        # print(data)
        # print("!!!!!!!!!!!!!!!!!!!!!", data['players'][0]['name'])
    
    print("\nSelect the attacker:\n")

    LEN_PLAYERS = len(data['players'])

    print("PLAYER LIST: ")
    for i in range(LEN_PLAYERS):
        print(i + 1 , "-", data['players'][i]['name'])
        time.sleep(1)
    
    print("\nENEMIES LIST: ")
    for i in range(len(data['enemies'])):
        print(i + 1 + LEN_PLAYERS, "-", data['enemies'][i]['name'])
        time.sleep(1)
    


    # Close file
    db.close()
    return 0


def display_hp():
    return 0


def display_atributes():
    return 0

def display_error(str):
    print(str)
    time.sleep(1)
    return 0


def main():
    print("Welcome to the combatRPG\nA cli tool to make the life of a Game Master easier\n")
    while True:
        print("=" * 20)
        print("\nSelect an option:")

        print("\n1. Attack\n2. Display hp of all characters\n3. Display atributes of all characters\n0. Exit")

        try:
            option = int(input())
        except ValueError:
            display_error("\nInvalid option!!\n")
            continue

        if option == 0:
            break
        elif option == 1:
            attack()
        elif option == 2:
            display_hp()
        elif option == 3:
            display_atributes()
        else:
            display_error("\nInvalid option!!\n")
            continue

        time.sleep(2)

main()

if '__name__' == '__main__':
    main()
