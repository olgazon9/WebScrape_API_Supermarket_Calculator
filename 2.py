import random
from enum import Enum
import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, filename='logfile.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} - Quantity: {self.quantity}"

class MenuOptions(Enum):
    PRINT_ALL_PRODUCTS = 1
    BUY_PRODUCT = 2
    SHOW_CART = 3
    SCRAPE_FOP_DESCRIPTION = 4  # New option for web scraping
    GET_CREDIT_CARD_INFO = 5  # New option for API call
    EXIT = 0

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product):
        self.items.append(product)
    
    def calculate_total(self):
        return sum(item.price for item in self.items)
    
    def __str__(self):
        cart_contents = "\n".join([f"{idx + 1}. {item}" for idx, item in enumerate(self.items)])
        total = self.calculate_total()
        return f"Shopping Cart:\n{cart_contents}\nTotal: ${total:.2f}"

def scrape_fop_description():
    url = "https://www.ocado.com/on-offer"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        fop_descriptions = soup.find_all(class_="fop-description")
        
        if not fop_descriptions:
            print("No 'fop-description' elements found on the page.")
        else:
            print("FOP Descriptions:")
            for idx, description in enumerate(fop_descriptions, start=1):
                print(f"{idx}. {description.text.strip()}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def api():
    url = "https://fake-credit-card-generator-json-api.p.rapidapi.com/credit-card"

    headers = {
        "X-RapidAPI-Key": "4ff8fb163amsh5d8992cd310fab2p158be0jsnbd9d20af0b89",
        "X-RapidAPI-Host": "fake-credit-card-generator-json-api.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        print("Credit Card Information:")
        print(f"Card Number: {data.get('card_number', 'N/A')}")
        print(f"Expiration Date: {data.get('expiration_date', 'N/A')}")
        print(f"Card Type: {data.get('card_type', 'N/A')}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def create_random_product():
    names = ["Apple", "Banana", "Orange", "Milk", "Bread", "Eggs", "Cheese", "Yogurt", "Chicken", "Rice"]
    name = random.choice(names)
    price = round(random.uniform(0.5, 10.0), 2)
    quantity = random.randint(1, 50)
    return Product(name, price, quantity)

def print_all_products(products):
    print("Supermarket Products:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product}")

def main():
    supermarket_products = []
    
    for _ in range(10):
        product = create_random_product()
        supermarket_products.append(product)
    
    shopping_cart = ShoppingCart()
    
    while True:
        logger.info("Displaying the menu.")
        print("\nMenu:")
        print("1. Print all products")
        print("2. Buy a product")
        print("3. Show shopping cart")
        print("4. Scrape 'fop-description' class from the website")
        print("5. Get credit card info from API")  # New option for API call
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == str(MenuOptions.PRINT_ALL_PRODUCTS.value):
            logger.info("User selected to print all products.")
            print_all_products(supermarket_products)
        elif choice == str(MenuOptions.BUY_PRODUCT.value):
            logger.info("User selected to buy a product.")
            print_all_products(supermarket_products)
            product_choice = int(input("Enter the number of the product you want to buy: ")) - 1
            if 0 <= product_choice < len(supermarket_products):
                logger.info("User selected a valid product to buy.")
                selected_product = supermarket_products[product_choice]
                shopping_cart.add_item(selected_product)
                logger.info(f"Added {selected_product.name} to the shopping cart.")
                print(f"Added {selected_product.name} to your shopping cart.")
            else:
                logger.warning("User provided an invalid product choice.")
                print("Invalid product choice.")
        elif choice == str(MenuOptions.SHOW_CART.value):
            logger.info("User selected to show the shopping cart.")
            print(shopping_cart)
        elif choice == str(MenuOptions.SCRAPE_FOP_DESCRIPTION.value):
            logger.info("User selected to scrape 'fop-description' class from the website.")
            scrape_fop_description()  # Call the scraping function here
        elif choice == str(MenuOptions.GET_CREDIT_CARD_INFO.value):
            logger.info("User selected to get credit card info from API.")
            api()  # Call the API function here
        elif choice == str(MenuOptions.EXIT.value):
            logger.info("User chose to exit the program.")
            print("Exiting the program.")
            break
        else:
            logger.warning("User selected an invalid choice.")
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
