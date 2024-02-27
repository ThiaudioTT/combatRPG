import time
import json
import os

# Se o resultado do ataque for igual ou maior que a CA do alvo, o ataque é bem-sucedido e o dano é determinado.
# return enemy HP
def calcCombat(d20AndMod, enemyArmor, enemyHp):
    # d20AndMod = d20 + modificador and other things
    if d20AndMod >= enemyArmor:
        diff = d20AndMod - enemyArmor
        enemyHp -= diff
        print("The attack was successful! The enemy lost ", diff, "HP")
    else:
        print("Miss/Block. No damage was done!")

    if enemyHp <= 0: print("The enemy is dead!")
    
    time.sleep(2)
    return enemyHp


def attack():
    # currPath = os.getcwd()
    # print("Current path: ", currPath)

    # TODO: verify if this path will chagne when the app is deployed
    with open('src/db.json', 'r') as db:
        data = json.load(db)
        # print(data)
        # print("!!!!!!!!!!!!!!!!!!!!!", data['players'][0]['name'])
    
    print("\nSelect the attacker and the defender:\n")

    LEN_PLAYERS = len(data['players'])

    print("PLAYER LIST: ")
    for i in range(LEN_PLAYERS):
        print(i + 1 , "-", data['players'][i]['name'])
        time.sleep(1)
    
    print("\nENEMIES LIST: ")
    for i in range(len(data['enemies'])):
        print(i + 1 + LEN_PLAYERS, "-", data['enemies'][i]['name'])
        time.sleep(1)
    

    try:
        attacker = int(input("\nAttacker: ")) - 1
        defender = int(input("Defender: ")) - LEN_PLAYERS
    except ValueError:
        display_error("\nInvalid option!!\n")
        return 0
    
    if min(attacker, defender) < 0 or max(attacker, defender) >= LEN_PLAYERS + len(data['enemies']):
        display_error("\nInvalid option!!\n")
        return 0
    
    player_atk = data['players'][attacker] if attacker < LEN_PLAYERS else data['enemies'][attacker - LEN_PLAYERS]
    player_def = data['players'][defender] if defender < LEN_PLAYERS else data['enemies'][defender - LEN_PLAYERS]


    print("\nAttacker: ", player_atk['name'])
    print("Defender: ", player_def['name'])
    time.sleep(2)


    try:
        print("\nSelect the dice number: ")
        dice = int(input())
        print("\nSelect the modifier: ")
        modifier = int(input())
    except ValueError:
        display_error("\nInvalid option!!\n")
        return 0
    

    defenderHp = calcCombat(dice + modifier, player_def['armor_class'], player_def['health'])

    # write into the db
    if defender < LEN_PLAYERS:
        data['players'][defender]['health'] = defenderHp
    else:
        data['enemies'][defender - LEN_PLAYERS]['health'] = defenderHp

    # write into the db
    with open('src/db.json', 'w') as db:
        json.dump(data, db, indent=4)
    
    # Close file
    db.close()
    return 0


def display_hp():
    with open('src/db.json', 'r') as db:
        data = json.load(db)
    
    print("\nPlayers: ")
    for i in range(len(data['players'])):
        print(data['players'][i]['name'], " - HP: ", data['players'][i]['health'])

    print("\nEnemies: ")
    for i in range(len(data['enemies'])):
        print(data['enemies'][i]['name'], " - HP: ", data['enemies'][i]['health'])
    
    print("\nPress any key to continue...")
    input()
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
