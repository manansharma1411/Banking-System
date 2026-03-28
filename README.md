# Banking-System

## Overview

A simple **Command Line Interface (CLI) Banking System** built using Python.
This project allows users to perform basic banking operations like:

* Create account
* Deposit money
* Withdraw money
* Check account balance

All data is stored persistently using a **JSON file**.


## Features

* Account creation
* Deposit function
* Withdrawal function
* Balance checking
* Persistent data storage (JSON)
* Error handling for invalid operations


## Project Structure

```
banking_system
│── main.py        
│── bank.py        
│── data.json
│── README.md      
```


## Tech Stack

* **Language:** Python
* **Storage:** JSON
* **Concepts Used:**

  * Object-Oriented Programming (OOP)
  * File Handling
  * CLI-based interaction


## Getting Started

### Clone the Repository

```
git clone https://github.com/your-username/banking-system.git
cd banking-system
```

### Run the Program

```
python main.py
```


## Usage

```
=== BANKING SYSTEM ===

1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
```


## Data Storage Example

```
{
    "Amit": 5000,
    "Rahul": 2000
}
```


## Future Enhancements

* PIN-based authentication
* Transaction history
* Database integration (SQLite/MySQL)
* AI-based expense analysis
* Financial insights dashboard


## Limitations

* No authentication system
* Local storage only
* No encryption for data
* Single-user oriented


## Contributing

Contributions are welcome!
Feel free to fork this repo and improve the project.
