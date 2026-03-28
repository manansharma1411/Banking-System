from bank import Bank

def main():
    bank = Bank()

    print("\n=== BANKING SYSTEM ===")

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter your name: ")
            bank.create_account(name)

        elif choice == 2:
            name = input("Enter your name: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(name, amount)

        elif choice == 3:
            name = input("Enter your name: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(name, amount)

        elif choice == 4:
            name = input("Enter your name: ")
            bank.check_balance(name)

        elif choice == 5:
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
