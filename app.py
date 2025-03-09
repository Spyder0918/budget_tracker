import json
import os

class BudgetTracker:
    
    def __init__(self, filename="budget_data.json"):
        """
        Initialize the BudgetTracker with a filename to store expenses.
        Load existing expenses if the file exists.
        """
        self.filename = filename
        self.expenses = self.load_data()

    def load_data(self):
        """
        Load expenses from a JSON file if it exists.
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_data(self):
        """
        Save the current list of expenses to a JSON file.
        """
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, category, amount, description):
        """
        Add a new expense to the list and save it.
        :param category: The category of the expense (e.g., Food, Rent)
        :param amount: The amount spent
        :param description: A brief description of the expense
        """
        expense = {"category": category, "amount": amount, "description": description}
        self.expenses.append(expense)
        self.save_data()
        print("Expense added successfully!")

    def view_expenses(self):
        """
        Display all recorded expenses in a formatted list.
        """
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        print("\nExpenses:")
        for idx, exp in enumerate(self.expenses, start=1):
            print(f"{idx}. {exp['category']} - ${exp['amount']:.2f} ({exp['description']})")
        
    def run(self):
        """
        Display a command-line menu for user interaction.
        """
        while True:
            print("\nBudget Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                category = input("Enter category: ")
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                self.add_expense(category, amount, description)
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    """
    Start the budget tracker when the script is run directly.
    """
    tracker = BudgetTracker()
    tracker.run()
