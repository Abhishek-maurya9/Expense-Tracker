# Expense Tracker 💰

A command-line Expense Tracker application built using **Python, Object-Oriented Programming (OOP), and JSON file handling**. It allows users to manage daily expenses, organize spending by category, track monthly expenses, and monitor their monthly budget.

The application uses JSON files for persistent storage, so expense records and budget information remain available even after restarting the program.

## 🚀 Features

### 1. Expense Management
- Add new expenses with title, amount, category, date, and description.
- View all recorded expenses.
- Update existing expense details.
- Delete expenses using their unique ID.
- Automatically generate unique expense IDs.

### 2. Expense Search
- Search expenses by category.
- Search expenses by a specific date.
- View expenses in chronological order.

### 3. Expense Analytics
- Calculate total expenses.
- Calculate expenses for a specific month.
- Generate category-wise spending summaries.

### 4. Budget Management
- Set a monthly spending budget.
- Calculate total spending for the current month.
- Display the remaining budget.
- Receive a warning when monthly expenses exceed the budget.

### 5. Data Persistence
- Store expense records in `expenses.json`.
- Store monthly budget information in `budget.json`.
- Automatically load saved data when the application starts.

### 6. Input Validation
- Prevent empty expense titles and categories.
- Validate expense amounts and budgets.
- Validate date formats.
- Handle invalid user input.
- Handle missing or malformed JSON files.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OOP | Application structure and data management |
| JSON | Persistent data storage |
| `os` | File existence checking |
| `pathlib` | File path management |
| `datetime` | Date validation and monthly filtering |
| `collections.defaultdict` | Category-wise expense aggregation |

## 📂 Project Structure

```text
Expense-Tracker/
│
├── main.py
│
├── expenses.json
│
├── budget.json
│
└── README.md
```

**Note:** The JSON files are created when the application saves expense or budget data.

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or above.
- Basic knowledge of running Python scripts from a terminal.

### 1. Clone the Repository

```bash
git clone https://github.com/Abhishek-maurya9/Expense-Tracker
```

### 2. Navigate to the Project Directory

```bash
cd Expense-Tracker
```

### 3. Run the Application

```bash
python main.py
```

No external Python packages are required. The application uses Python's built-in libraries.

## 📸 Application Menu

```text
================================
       EXPENSE TRACKER
================================

1. Add Expense
2. View All Expenses
3. Search by Category
4. Search by Date
5. Update Expense
6. Delete Expense
7. Total Expenses
8. Monthly Expenses
9. Category Summary
10. Set Monthly Budget
11. Check Monthly Budget
0. Exit

================================
Enter your choice:
```

## 🧠 OOP Concepts Implemented

The project follows an object-oriented design with three main components.

**1. Expense Class**
- Represents an individual expense.
- Stores expense attributes.
- Converts expense objects into dictionaries using `to_dict()`.
- Reconstructs expense objects from dictionaries using the `@classmethod` decorator and `from_dict()`.

**2. Storage Class**
- Handles JSON file operations.
- Loads and saves expense records.
- Loads and saves budget information.
- Uses static methods because storage operations do not require instance-specific state.

**3. ExpenseManager Class**
- Manages the application's business logic.
- Handles CRUD operations.
- Performs expense calculations and summaries.
- Manages budget tracking.
- Communicates with the Storage class for persistent data management.

## 🔮 Future Improvements

Potential enhancements for future versions:

- [ ] Monthly and yearly financial reports.
- [ ] Expense visualization using Matplotlib.
- [ ] Export expense reports to CSV and Excel.
- [ ] Separate budgets for individual categories.
- [ ] User authentication and multiple accounts.
- [ ] SQLite database integration.
- [ ] GUI using Tkinter or a web interface using Flask/FastAPI.
- [ ] Automated recurring expense tracking.

## 🎯 Learning Outcomes

Through this project, I practiced:

- Object-Oriented Programming in Python.
- Classes, objects, instance methods, static methods, and class methods.
- File handling and JSON serialization/deserialization.
- CRUD operations.
- Exception handling and input validation.
- Working with dates using `datetime`.
- Data aggregation using `defaultdict`.
- Separating application logic from storage operations.

---

⭐ If you find this project useful, consider giving it a star!
