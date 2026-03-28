import json
import os

class Bank:
    def __init__(self):
        self.file = "data.json"
        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                json.dump({}, f)

    def load_data(self):
        with open(self.file, 'r') as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=4)

    def create_account(self, name):
        data = self.load_data()
        if name in data:
            print("Account already exists!")
        else:
            data[name] = 0
            self.save_data(data)
            print("Account created successfully!")

    def deposit(self, name, amount):
        data = self.load_data()
        if name in data:
            if amount > 0:
                data[name] += amount
                self.save_data(data)
                print("Deposit successful!")
                print(f"Balance: ₹{data[name]}")
            else:
                print("Invalid amount!")
        else:
            print("Account not found!")

    def withdraw(self, name, amount):
        data = self.load_data()
        if name in data:
            if amount <= data[name]:
                data[name] -= amount
                self.save_data(data)
                print("Withdrawal successful!")
                print(f"Balance: ₹{data[name]}")
            else:
                print("Insufficient balance!")
        else:
            print("Account not found!")

    def check_balance(self, name):
        data = self.load_data()
        if name in data:
            print(f"Balance: ₹{data[name]}")
        else:
            print("Account not found!")
