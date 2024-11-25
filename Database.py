import sqlite3

class Database:
    def __init__(self, db_name="budget.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    salary REAL DEFAULT 0.0
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    name TEXT,
                    amount REAL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS goals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    goal TEXT,
                    amount REAL,
                    months_needed INTEGER,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            """)

    def add_user(self, username, password):
        try:
            with self.conn:
                self.conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                print(f"User {username} registered successfully!")
        except sqlite3.IntegrityError:
            print("Username already exists!")

    def get_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        return cursor.fetchone()

    def set_salary(self, user_id, salary):
        with self.conn:
            self.conn.execute("UPDATE users SET salary = ? WHERE id = ?", (salary, user_id))

    def add_expense(self, user_id, name, amount):
        with self.conn:
            self.conn.execute("INSERT INTO expenses (user_id, name, amount) VALUES (?, ?, ?)", (user_id, name, amount))

    def add_goal(self, user_id, goal, amount, months_needed):
        with self.conn:
            self.conn.execute(
                "INSERT INTO goals (user_id, goal, amount, months_needed) VALUES (?, ?, ?, ?)",
                (user_id, goal, amount, months_needed)
            )

    def get_expenses(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name, amount FROM expenses WHERE user_id = ?", (user_id,))
        return cursor.fetchall()

    def get_goal(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT goal, amount, months_needed FROM goals WHERE user_id = ?", (user_id,))
        return cursor.fetchone()

    def get_salary(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT salary FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()[0]