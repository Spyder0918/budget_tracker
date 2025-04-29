import json
import os
import csv


class BudgetTracker:
    
    def __init__(self, filename="budget_data.json"):
        """
        Initialize the BudgetTracker with a filename to store expenses.
        Load existing expenses if the file exists.
        """
        self.filename = filename
        self.expenses = self.load_data()  # Load saved expenses from file

    def load_data(self):
        """
        Load expenses from a JSON file if it exists.
        """
        if os.path.exists(self.filename):  # Check if the file exists
            with open(self.filename, "r") as file:
                return json.load(file)  # Load and return expenses from the file
        return []  # Return empty list if no file exists

    def save_data(self):
        """
        Save the current list of expenses to a JSON file.
        """
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)  # Write expenses to file with indentation

    def add_expense(self, category, amount, description):
        """
        Add a new expense to the list and save it.
        :param category: The category of the expense (e.g., Food, Rent)
        :param amount: The amount spent
        :param description: A brief description of the expense
        """
        expense = {
            "category": category,
            "amount": amount,
            "description": description
        }
        self.expenses.append(expense)  # Add new expense to the list
        self.save_data()  # Save updated list to file
        print("Expense added successfully!")

    def view_expenses(self):
        """
        Display all recorded expenses in a formatted list.
        """
        if not self.expenses:
            print("No expenses recorded.")  # Inform user if no expenses exist
            return
        
        print("\nExpenses:")
        for idx, exp in enumerate(self.expenses, start=1):  # Print each expense with index
            print(f"{idx}. {exp['category']} - ${exp['amount']:.2f} ({exp['description']})")
        
    def delete_last_expense(self):
        """
        Delete the last recorded expense, if any exist.
        """
        if not self.expenses:
            print("No expenses to delete.")  # Handle case with no expenses
            return
        removed = self.expenses.pop()  # Remove the last expense from the list
        self.save_data()  # Save the updated list
        print(f"Deleted last expense: {removed['category']} - ${removed['amount']:.2f} ({removed['description']})")

    def export_to_csv(self, csv_filename="budget_export.csv"):
        """
        Export the list of expenses to a CSV file.
        :param csv_filename: The name of the CSV file to write to.
        """
        if not self.expenses:
            print("No expenses to export.")
            return
        
        with open(csv_filename, "w", newline='') as csvfile:
            fieldnames = ["category", "amount", "description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # Write CSV column headers
            for expense in self.expenses:
                writer.writerow(expense)  # Write each expense as a row

        print(f"Expenses exported successfully to '{csv_filename}'")

    def run(self):
        """
        Display a command-line menu for user interaction.
        """
        while True:
            # Display menu options
            print("\nBudget Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Delete Last Expense")
            print("4. Export to CSV")
            print("5. Exit")
            choice = input("Choose an option: ")
            
            # Process user choice
            if choice == "1":
                category = input("Enter category: ")
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                self.add_expense(category, amount, description)
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.delete_last_expense()
            elif choice == "4":
                self.export_to_csv()
            elif choice == "5":
                print("Goodbye!")  # Exit the loop and program
                break
            else:
                print("Invalid choice. Try again.")  # Handle invalid input

if __name__ == "__main__":
    """
    Start the budget tracker when the script is run directly.
    """
    tracker = BudgetTracker()
    tracker.run()  # Launch the main interactive menu
