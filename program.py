import accounts

def menu_loop():
    currentObject = accounts.currentAccount()
    savingsObject = accounts.savingsAccount()

    while True:

        print("1. Current Account")
        print("2. Savings Account")
        menu_option = int(input("CHOOSE [1] OR [2]: "))

        if menu_option == 1:
            print("1. Deposit funds")
            print("2. Withdraw funds")
            submenu_option = int(input("CHOOSE [1] OR [2]: "))

            if submenu_option == 1:
                value = int(input("How much would you like to deposit? "))
                currentObject.deposit(value)

            elif submenu_option == 2:
                value = int(input("How much would you like to withdraw?"))
                currentObject.withdraw(value)
            else:
                print("Wrong menu choice!")

        elif menu_option == 2:
            print("1. Deposit funds")
            print("2. Withdraw funds")
            submenu_option = int(input("CHOOSE [1] OR [2]: "))

            if submenu_option == 1:
                value = int(input("How much would you like to deposit? "))
                savingsObject.deposit(value)

            elif submenu_option == 2:
                value = int(input("How much would you like to withdraw?"))
                savingsObject.withdraw(value)

            else:
                print("Wrong menu choice!")

        else:
            print("Wrong menu choice!")

        print()


def main():
    menu_loop()


if __name__ == '__main__':
    main()
