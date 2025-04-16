class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance is ${self.balance}.")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"${amount} withdrawn. New balance is ${self.balance}.")

    def get_balance(self):
        return self.balance

def main():
    account = BankAccount("John Doe")
    print("Welcome,", account.account_holder)
    while True:
        action = input("What would you like to do? (deposit/withdraw/exit): ").lower()
        if action == 'deposit':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif action == 'withdraw':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif action == 'exit':
            print("Thank you for banking with us.")
            break
        else:
            print("Invalid action. Please choose deposit, withdraw, or exit.")

if __name__ == "__main__":
    main()