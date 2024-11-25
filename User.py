class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username

    def set_salary(self, salary, db):
        query = "UPDATE users SET salary = %s WHERE id = %s"
        db.execute(query, (salary, self.id))
        print(f"Salary set to {salary} for user {self.username}")

    def add_expense(self, name, amount, db):
        query = "INSERT INTO expenses (user_id, expense_name, amount) VALUES (%s, %s, %s)"
        db.execute(query, (self.id, name, amount))
        print(f"Added expense: {name} - {amount}")

    def set_goal(self, goal_name, goal_amount, months_needed, db):
        query = "INSERT INTO goals (user_id, goal_name, goal_amount, months_needed) VALUES (%s, %s, %s, %s)"
        db.execute(query, (self.id, goal_name, goal_amount, months_needed))
        print(f"Goal '{goal_name}' set to reach {goal_amount} in {months_needed} months")