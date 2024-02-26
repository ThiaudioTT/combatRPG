import time

def attack():
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

main()

if '__name__' == '__main__':
    main()
