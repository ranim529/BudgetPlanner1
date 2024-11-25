from BudgetPlanner import BudgetPlanner
from Database import Database
from colorama import Fore,init

init(autoreset=True)


def main():
    db = Database()
    planner = BudgetPlanner(db)
    print(Fore.GREEN + "Connected to database successfully!")
    print(Fore.GREEN + "Program started...")

    while True:
        print(Fore.YELLOW + "\n1. Sign Up")
        print(Fore.BLUE + "2. Login")
        print(Fore.MAGENTA + "3. Set Salary")
        print(Fore.CYAN + "4. Add Expenses")
        print(Fore.LIGHTGREEN_EX + "5. Add Goal")
        print(Fore.LIGHTWHITE_EX + "6. Show Summary")
        print(Fore.RED + "7. Exit")
        choice = input(Fore.LIGHTYELLOW_EX + "Choose an option: ")

        if choice == "1":
            print(Fore.MAGENTA + "Registering a new user...")
            planner.sign_up()
        elif choice == "2":
            print(Fore.BLUE + "Logging in...")
            planner.login()
        elif choice == "3":
            print(Fore.MAGENTA + "Setting salary...")
            planner.set_salary()
        elif choice == "4":
            print(Fore.CYAN + "Adding an expense...")
            planner.add_expense()
        elif choice == "5":
            print(Fore.LIGHTGREEN_EX + "Setting a financial goal...")
            planner.add_goal()
        elif choice == "6":
            print(Fore.LIGHTWHITE_EX + "Displaying budget summary...")
            planner.show_summary()
        elif choice == "7":
            print(Fore.RED + "Exiting program...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again")

if __name__ == "__main__":
    main()