# Math Operations and Supermarket Menu

This repository contains two Python programs: `operations.py` and `supermarket_menu.py`, each with its own purpose and functionality.

## 1. `operations.py`

### Description
The `operations.py` program performs basic mathematical operations on two numbers: addition, subtraction, multiplication, and division. It also logs the operations and their results to a file named `operations.log`.

### Usage
1. Run the program using Python.
2. Input two numbers when prompted.
3. The program will perform the following operations:
   - Addition
   - Subtraction
   - Multiplication
   - Division (with error handling for division by zero)
4. The results of these operations are displayed, and the logging information is saved to `operations.log`.

### Requirements
- Python 3.x
- `logging` library

## 2. `supermarket_menu.py`

### Description
The `supermarket_menu.py` program simulates a simple supermarket menu and shopping cart system. It allows users to interact with the menu by selecting options to view products, add products to their shopping cart, and perform other actions like web scraping and API calls.

### Usage
1. Run the program using Python.
2. Choose from the following options:
   - Print all products available in the supermarket.
   - Buy a product and add it to the shopping cart.
   - Show the contents of the shopping cart.
   - Scrape 'fop-description' class from a website (web scraping).
   - Get credit card information from an API.
   - Exit the program.
3. Follow the on-screen instructions to perform the chosen action.
4. The program will log user interactions in `logfile.log`.

### Requirements
- Python 3.x
- Libraries:
  - `logging`
  - `requests`
  - `bs4` (Beautiful Soup)

## Important Notes
- Ensure you have the necessary libraries installed before running the programs.
- The logging files (`operations.log` and `logfile.log`) will contain information about program activities.
- Make sure you have an active internet connection for the web scraping and API functionalities in `supermarket_menu.py`.

Feel free to explore and use these Python programs as needed. If you encounter any issues or have questions, refer to the program-specific documentation within the code or seek further assistance.

