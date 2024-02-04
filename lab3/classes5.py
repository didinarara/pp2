class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds. Withdrawal cannot exceed available balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

if __name__ == "__main__":
    my_account = Account(owner="John Doe", balance=1000)

    my_account.deposit(500)
    my_account.withdraw(200)
    my_account.withdraw(800)
    my_account.deposit(1000)

    my_account.withdraw(1500)
