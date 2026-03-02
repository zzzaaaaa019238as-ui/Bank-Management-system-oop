class BankAccount:
    def __init__(self, account_number, owner, balance, password):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.password = password

    def deposit(self, amount):
        self.balance += amount
        print(f"Success! New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Success! Remaining: {self.balance}")
        else:
            print("Error: Insufficient balance!")

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Success! Transferred {amount} to {target_account.owner}")
        else:
            print("Error: Insufficient balance!")

    def show_balance(self):
        print(f"Current balance: {self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, acc_num, owner, balance, password):
        if acc_num in self.accounts:
            print("Account already exists!")
        else:
            new_acc = BankAccount(acc_num, owner, balance, password)
            self.accounts[acc_num] = new_acc
            print(f"Account created for {owner}")

    def get_account(self, acc_num):
        return self.accounts.get(acc_num)

    def view_all_accounts(self):
        for acc in self.accounts.values():
            print(f"Acc: {acc.account_number} | Owner: {acc.owner} | Balance: {acc.balance}")


my_bank = Bank("Bank Masr")

while True:
    print(f"\n--- {my_bank.name} Management System ---")
    print("1. Create new account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Show Balance")
    print("6. Exit")

    choice = input("Choose your operation: ")

    if choice == '1':
        acc_num = input("Account Number: ")
        name = input("Owner Name: ")
        bal = float(input("Initial Balance: "))
        pwd = input("Set Password: ")
        my_bank.create_account(acc_num, name, bal, pwd)

    elif choice == '2':
        acc_num = input("Account Number: ")
        acc = my_bank.get_account(acc_num)
        if acc:
            amt = float(input("Deposit Amount: "))
            acc.deposit(amt)
        else:
            print("Account not found!")

    elif choice == '3':
        acc_num = input("Account Number: ")
        acc = my_bank.get_account(acc_num)
        if acc:
            pwd = input("Enter Password: ")
            if pwd == acc.password:
                amt = float(input("Withdraw Amount: "))
                acc.withdraw(amt)
            else:
                print("Wrong Password!")
        else:
            print("Account not found!")

    elif choice == '4':
        sender_num = input("Your Account Number: ")
        sender = my_bank.get_account(sender_num)
        if sender:
            pwd = input("Enter Password: ")
            if pwd == sender.password:
                receiver_num = input("Receiver Account Number: ")
                receiver = my_bank.get_account(receiver_num)
                if receiver:
                    amt = float(input("Transfer Amount: "))
                    sender.transfer(receiver, amt)
                else:
                    print("Receiver not found!")
            else:
                print("Wrong Password!")
        else:
            print("Account not found!")

    elif choice == '5':
        acc_num = input("Account Number: ")
        acc = my_bank.get_account(acc_num)
        if acc:
            acc.show_balance()
        else:
            print("Account not found!")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
