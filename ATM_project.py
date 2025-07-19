# Simple ATM Money Transaction System

# Initial account details
account_balance = 10000
pin_code = "6679"

# Function to display ATM menu
def show_menu():
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# Main function
def atm():
    global account_balance
    print("Welcome to the ATM!")

    # PIN verification
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")
        if pin == pin_code:
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN! Attempts left: {attempts}")
    else:
        print("Too many incorrect attempts. Exiting...")
        return

    # Menu loop
    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            print(f"Your current balance is ₹{account_balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                account_balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid amount!")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if 0 < amount <= account_balance:
                account_balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount!")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid option! Please select from 1 to 4.")
            continue

# Run the ATM program
atm()