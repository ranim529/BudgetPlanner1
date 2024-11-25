from colorama import Fore


class BudgetPlanner:
    def __init__(self, db):
        self.db = db
        self.user_id = None

    def sign_up(self):
        username = input(Fore.MAGENTA + "Enter a username: ")
        password = input(Fore.MAGENTA + "Enter a password: ")
        self.db.add_user(username, password)

    def login(self):
        username = input(Fore.BLUE + "Enter your username: ")
        password = input(Fore.BLUE + "Enter your password: ")
        user = self.db.get_user(username, password)
        if user:
            self.user_id = user[0]
            print(Fore.GREEN + f"Welcome back, {username}!")
        else:
            print(Fore.RED + "Invalid username or password")

    def set_salary(self):
        if self.user_id:
            salary = float(input(Fore.MAGENTA + "Enter your monthly salary: "))
            self.db.set_salary(self.user_id, salary)
            print(Fore.GREEN + f"Salary set to {salary}")
        else:
            print(Fore.RED + "No user logged in")

    def add_expense(self):
        if self.user_id:
            expense_name = input(Fore.CYAN + "Enter expense name: ")
            amount = float(input(Fore.CYAN + "Enter expense amount: "))
            self.db.add_expense(self.user_id, expense_name, amount)
            print(Fore.GREEN + f"Added expense: {expense_name} - {amount}")
        else:
            print(Fore.RED + "No user logged in.")

    def add_goal(self):
        if self.user_id:
            goal = input(Fore.LIGHTGREEN_EX + "Enter your goal (exp: Car, House): ")
            goal_amount = float(input(Fore.LIGHTGREEN_EX + f"How much does your {goal} cost? "))
            while True:
                months_needed = int(input(Fore.LIGHTGREEN_EX + "In how many months do you want to achieve this goal? "))
                if months_needed > 0:
                    print(Fore.GREEN + f"Months to achieve goal: {months_needed}")
                    break
                else:
                    print(Fore.RED + "Months needed must be greater than 0. Please enter a valid number")

            self.db.add_goal(self.user_id, goal, goal_amount, months_needed)
            print(Fore.GREEN + f"Goal '{goal}' set to reach {goal_amount} in {months_needed} months")
        else:
            print(Fore.RED + "No user logged in")

    def show_summary(self):
        if self.user_id:
            print(Fore.LIGHTWHITE_EX + "\n--- Budget Summary ---")
            salary = self.db.get_salary(self.user_id)
            print(Fore.LIGHTWHITE_EX + f"Salary: {salary}")

            expenses = self.db.get_expenses(self.user_id)
            total_expenses = sum(amount for _, amount in expenses)
            print(Fore.LIGHTCYAN_EX + "Expenses:")
            for name, amount in expenses:
                print(Fore.LIGHTCYAN_EX + f"- {name}: {amount}")
            remaining = salary - total_expenses
            print(Fore.LIGHTWHITE_EX + f"Total Expenses: {total_expenses}")
            print(Fore.LIGHTWHITE_EX + f"Remaining after expenses: {remaining}")

            goal = self.db.get_goal(self.user_id)
            if goal:
                goal_name, goal_amount, months_needed = goal
                print(Fore.LIGHTGREEN_EX + f"Goal: {goal_name}")
                print(Fore.LIGHTGREEN_EX + f"Goal Amount: {goal_amount}")
                print(Fore.LIGHTGREEN_EX + f"Months Needed: {months_needed}")
                monthly_savings = goal_amount / months_needed
                recommended_spending = salary - monthly_savings
                print(Fore.LIGHTGREEN_EX + f"Monthly Savings Needed: {monthly_savings}")
                print(Fore.LIGHTWHITE_EX + f"Recommended Monthly Spending: {recommended_spending}")
            print(Fore.LIGHTWHITE_EX + "----------------------")
        else:
            print(Fore.RED + "No user logged in")


