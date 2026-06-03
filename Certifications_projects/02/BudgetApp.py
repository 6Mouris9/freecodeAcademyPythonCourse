class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for entry in self.ledger:
            description = entry["description"][:23]
            amount = entry["amount"]
            total += amount
            items += f"{description:<23}{amount:>7.2f}\n"
        output = title + items + f"Total: {self.get_balance():.2f}"
        
        return output

    def deposit(self, amount = 0.0, description=''):
        amount = float(amount)
        if not isinstance(amount, float) and not isinstance(amount, int):
            print("Amount must be a digit")
            return False
        if not amount >= 0:
            print("The value must be greater than 0.") 
            return
        if not isinstance(description, str):
            print("The description must be a text.")
            return
        # ------------------------------------------
        self.ledger.append({'amount': amount, 'description': description})
        return True

    def withdraw(self, amount = 0.0, description =''):
        if not self.check_funds(amount):
            return False
        if not isinstance(description, str):
            print("The description must be a text.")
            return False
        # -------------------------------------------
        amount = (-amount)
        self.ledger.append({'amount': amount, 'description': description})
        return True

    def get_balance(self):
        total = 0.0
        for item in self.ledger:
            total += item['amount']
        return total

    def check_funds(self, amount):
        amount = float(amount)
        if not isinstance(amount, float) and not isinstance(amount, int):
            print("Amount must be a digit")
            return False
        if not amount >= 0:
            print("The value must be greater than 0.") 
            return False
        if amount > self.get_balance():
            print("Error: amount is greater than total")
            return False
        else:
            return True
    
    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True
        
    
def create_spend_chart(categories):

    # calcular gastos
    spent = []

    for category in categories:
        total = 0

        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])

        spent.append(total)

    total_spent = sum(spent)

    # porcentagens arredondadas para baixo
    percentages = []

    for value in spent:
        percent = (value / total_spent) * 100
        percent = int(percent // 10) * 10
        percentages.append(percent)

    # construção do gráfico
    chart = "Percentage spent by category\n"

    # barras
    for i in range(100, -1, -10):

        chart += str(i).rjust(3) + "| "

        for percent in percentages:

            if percent >= i:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    # linha horizontal
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # nomes das categorias
    names = [category.name for category in categories]

    max_len = max(len(name) for name in names)

    for i in range(max_len):

        chart += "     "

        for name in names:

            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "

        chart += "\n"

    # remover último \n
    return chart[:-1]
    
    


