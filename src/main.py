import time
import json
import os
import colors

CUR_PATH = os.path.dirname(os.path.abspath(__file__))

# Se o resultado do ataque for igual ou maior que a armadura do alvo, o ataque é bem-sucedido e o dano é determinado.
# return enemy HP
def calcCombat(d20AndMod: int, enemyArmor: int, enemyHp: int) -> int:
    # d20AndMod = d20 + modificador and other things
    if d20AndMod >= enemyArmor:
        diff = d20AndMod - enemyArmor
        enemyHp -= diff
        print(colors.RED + "🩸 The attack was successful! The opponent lost", diff, "HP 🩸")
    else:
        print(colors.WHITE + "🛡️ 🛡️ Miss/Block. No damage was done! 🛡️ 🛡️")

    if enemyHp <= 0: print(colors.BLUE + "💀 The opponent is dead! 💀")
    
    time.sleep(2)
    return enemyHp


def attack():
    with open(CUR_PATH + '/db.json', 'r') as db:
        data = json.load(db)

    if len(data['players']) == 0 or len(data['enemies']) == 0:
        display_error(colors.RED + "\nThere are no players or enemies to attack!\n")
        return 0
    
    print(colors.YELLOW + "\nSelect the attacker and the defender:\n")

    LEN_PLAYERS = len(data['players'])

    print(colors.GREEN + "🕹️ PLAYER LIST: ")
    for i in range(LEN_PLAYERS):
        print(colors.GREEN + "  ", i + 1 , "-", data['players'][i]['name'], end=" ")
        if data['players'][i]['health'] <= 0: print(colors.RED + "(DEAD 💀)", end="")
        print("")
        time.sleep(0.5)
    
    print(colors.RED + "\n👹 ENEMIES LIST: ")
    for i in range(len(data['enemies'])):
        print("  ", i + 1 + LEN_PLAYERS, "-", data['enemies'][i]['name'], end=" ")
        if data['enemies'][i]['health'] <= 0: print("(DEAD 💀)", end="")
        print("")
        time.sleep(0.5)
    
    print(colors.RESET)
    try:
        attackerIdx = int(input("\n🔪 Attacker: ")) - 1
        # DefenderIdx is defenderIdx > attackerIdx
        defenderIdx = int(input("🛡️ Defender: ")) - 1
    except ValueError:
        display_error("\nInvalid option!!\n")
        return 0
    
    if min(attackerIdx, defenderIdx) < 0 or max(attackerIdx, defenderIdx) >= LEN_PLAYERS + len(data['enemies']):
        display_error("\nInvalid option!!\n")
        return 0
    
    player_atk = data['players'][attackerIdx] if attackerIdx < LEN_PLAYERS else data['enemies'][attackerIdx - LEN_PLAYERS]
    player_def = data['players'][defenderIdx] if defenderIdx < LEN_PLAYERS else data['enemies'][defenderIdx - LEN_PLAYERS]


    print(colors.YELLOW + "\nℹ️ ", player_atk['name'] + " is attacking " + player_def['name'] + "!")
    time.sleep(2)

    try:
        dice = int(input("\n🎲 Select the dice number: "))
        modifier = int(input("\n🍀 Select the modifier: "))
    except ValueError:
        display_error("\nInvalid option!!\n")
        return 0
    

    defenderHp = calcCombat(dice + modifier, player_def['armor_class'], player_def['health'])

    # write into the db
    if defenderIdx < LEN_PLAYERS:
        data['players'][defenderIdx]['health'] = defenderHp
    else:
        data['enemies'][defenderIdx - LEN_PLAYERS]['health'] = defenderHp

    # write into the db
    with open(CUR_PATH + '/db.json', 'w') as db:
        json.dump(data, db, indent=4)
    
    return 0


def display_hp():
    with open(CUR_PATH + '/db.json', 'r') as db:
        data = json.load(db)
    
    print(colors.GREEN + "\n🕹️ Players: ")
    for i in range(len(data['players'])):
        print("  ", data['players'][i]['name'], " - HP: ", data['players'][i]['health'])

    print(colors.RED + "\n👹 Enemies: ")
    for i in range(len(data['enemies'])):
        print("  ",data['enemies'][i]['name'], " - HP: ", data['enemies'][i]['health'])
    
    print(colors.YELLOW)
    print("\nPress any key to continue...")
    input()
    return 0


def display_atributes():
    with open(CUR_PATH + '/db.json', 'r') as db:
        data = json.load(db)

    print("\nPlayers: ")
    for i in range(len(data['players'])):
        for key in data['players'][i]:
            print(key, ":", data['players'][i][key])
        time.sleep(1)
        print("\n")
    
    print("\nEnemies: ")
    for i in range(len(data['enemies'])):
        for key in data['enemies'][i]:
            print(key, ":", data['enemies'][i][key])
        time.sleep(1)
        print("\n")
    
    print("\nPress any key to continue...")
    input()

    return 0

def display_error(str):
    print(str)
    time.sleep(1)
    return 0


def main():
    print(colors.RED + "⚔️ ⚔️ Welcome to the combatRPG 🛡️ 🛡️ \n" + colors.WHITE + "A cli tool to make the life of a Game Master easier\n" + colors.RESET)
    time.sleep(3)
    while True:
        print(colors.RESET + "=" * 40)
        print("\nSelect an option:")

        print("\n1. ⚔️ Attack\n2. 🩹 Display hp of all characters\n3. ☘️ Display atributes of all characters \n0. 👣 Exit \n")

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
