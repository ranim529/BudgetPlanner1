from BudgetPlanner import BudgetPlanner
from Database import Database
from colorama import Fore,init

init(autoreset=True)


def main():
    db = Database()
    planner = BudgetPlanner(db)
    print(Fore.GREEN + "Welcome to our program!")
    print(Fore.GREEN + "Budget Planner")

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
            planner.sign_up()
        elif choice == "2":
            planner.login()
        elif choice == "3":
            planner.set_salary()
        elif choice == "4":
            planner.add_expense()
        elif choice == "5":
            planner.add_goal()
        elif choice == "6":
            planner.show_summary()
        elif choice == "7":
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again")

if __name__ == "__main__":
    main()