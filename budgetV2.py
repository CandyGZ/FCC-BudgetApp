# Esta versión entrega los resultados pero el requerimiento es
# que la tabla se debe imprimir en una sola cadena con saltos de linea,
# incluyendo el título o encabezado de la categoría
from math import ceil, floor


class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.funds = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount
        print(self.name, description, amount)

    def withdraw(self, amount, description=" "):
        funds = self.check_funds(amount)
        if funds:
            self.ledger.append({"amount": -amount, "description": description})
            self.funds -= amount
            return True
        else:
            return False

    def get_balance(self):
        print(self.funds)
        return self.funds

    def transfer(self, amount, cat_destino):
        funds = self.check_funds(amount)
        if funds:
            self.ledger.append(
                {
                    "amount": -amount,
                    "description": "Transfer to {}".format(cat_destino.name),
                }
            )  # format trae los valores y los mete en donde se colocan {}
            self.funds -= amount
            cat_destino.funds += amount
            cat_destino.ledger.append(
                {
                    "amount": amount,
                    "description": "Transfer from {}".format(self.name),
                }
            )

            print(self.ledger[-1]["description"], self.ledger[-1]["amount"])
            return True
        else:
            print("not enought money, sorry")
            return False

    def check_funds(self, amount):
        if self.funds >= amount:
            return True
        else:
            return False


import math


def create_spend_chart(categories):
    # Calculate the total withdrawals for each category.
    category_totals = [
        sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        for category in categories
    ]
    total_spent = sum(category_totals)

    # Calculate the percentages and round up to the nearest 10.
    percentages = [math.ceil(total / total_spent * 100) for total in category_totals]

    # Build the bar chart.
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        chart += " ".join(
            "o " if percentage >= i else "  " for percentage in percentages
        )
        chart += " \n"

    chart += (
        "    -" + "---" * len(categories) + "\n"
    )  # imprime la linea sobre las categorías

    # Find the longest category name.
    max_name_length = max(len(category.name) for category in categories)

    # Add category names vertically below the bars.
    for i in range(max_name_length):
        chart += "     "
        chart += (
            "  ".join(  # aqui está el espacio entre categorías,actualmente 2 espacios
                category.name[i] if i < len(category.name) else " "
                for category in categories
            )
        )
        chart += " \n"

    print(chart.rstrip("\n"))
    return chart.rstrip("\n")

    # total = 0
    # new_list = []
    # for category in list_categories:
    #     # print(category.funds)
    #     total_cat = 0
    #     for transaction in category.ledger:  # calculo el total gastado por categoria
    #         if transaction["amount"] < 0:
    #             # print(transaction["amount"], transaction["description"])
    #             total_cat += transaction["amount"]
    #     print(category.name, total_cat)
    #     new_list.append(category.name)
    #     new_list.append(total_cat)
    #     total += total_cat
    # print(total)
    # print(new_list)

    # num_ele = (len(new_list)) // 2
    # # print(num_ele)
    # i = 1
    # percentages = []
    # for element in range(num_ele):
    #     value = new_list[i]
    #     # print(value)
    #     percentage = (value * 100) // total
    #     percentages.append(percentage)
    #     i += 2
    # print(percentages)

    # # imprimir chart
    # print("Percentage spent by category")
    # for category in new_list:
    #     i = 100
    #     j = 1
    #     for number in new_list:
    #         if i == (new_list[j]) * 100 // total:
    #             print(f"({i}|  o)")


def print_budget(Category):
    # Calculate the total amount in the budget category.
    total = sum(transaction["amount"] for transaction in Category.ledger)
    # Create a title line.
    anchor = len(Category.name)
    symbols = (30 - anchor) // 2
    title = "*" * symbols
    title += Category.name
    title += "*" * symbols
    # Print the title line.
    print(title)
    # Iterate over the ledger and print each transaction on a separate line.
    for transaction in Category.ledger:
        description = transaction["description"]
        amount = transaction["amount"]
        # Truncate the description to 23 characters.
        if len(description) > 23:
            description = description[:23]
        else:
            space = (
                23 - len(description)
            ) * " "  # el 2 es por los dos decimales que se agregan al final
            description = description + space

        amount = format(amount, ".2f").rjust(7)
        # Print the transaction.
        print("{}{}".format(description, amount))
    # Print a line displaying the category total.
    print("Total: {:.2f}".format(total))


food = Category("Food")
health = Category("Health")
entertainment = Category("Entertainment")
food.deposit(900, "deposit")
# food.deposit(50.34, " ")
print(food.funds)
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
print(food.funds)
school = Category("School")
food.transfer(20, entertainment)
# food.transfer(100, school)
school.withdraw(100, "book")
entertainment.deposit(2000, "initial deposit")
entertainment.withdraw(1700, "Movies")
print(food.funds, school.funds)
print_budget(food)
print_budget(school)
create_spend_chart([food, school, entertainment, health])
