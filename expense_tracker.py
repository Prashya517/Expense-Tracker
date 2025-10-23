import csv
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = input("Enter category (Food, Travel, Shopping, Bills, etc.): ")
    amount = float(input("Enter amount: ₹"))
    description = input("Enter short description: ")

    with open(FILENAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            print("\n📘 All Expenses:\n")
            print(f"{'Date':<20}{'Category':<15}{'Amount':<10}{'Description'}")
            print("-" * 60)
            for row in reader:
                print(f"{row[0]:<20}{row[1]:<15}₹{row[2]:<10}{row[3]}")
    except FileNotFoundError:
        print("⚠️ No expenses recorded yet.\n")

def show_summary():
    try:
        totals = {}
        total_amount = 0
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                totals[category] = totals.get(category, 0) + amount
                total_amount += amount

        print("\n📊 Expense Summary:\n")
        for cat, amt in totals.items():
            print(f"{cat:<15}: ₹{amt:.2f}")
        print("-" * 30)
        print(f"Total Spent: ₹{total_amount:.2f}\n")

    except FileNotFoundError:
        print("⚠️ No data to summarize.\n")

def main():
    print("💰 SIMPLE EXPENSE TRACKER 💰\n")
    print("Data will be saved in 'expenses.csv'\n")

    while True:
        print("1️⃣ Add Expense")
        print("2️⃣ View All Expenses")
        print("3️⃣ Show Summary")
        print("4️⃣ Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
