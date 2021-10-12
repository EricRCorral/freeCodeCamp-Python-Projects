class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        totalAmount = 0
        for item in self.ledger:
            totalAmount += item['amount']
        return totalAmount

    def withdraw(self, amount, description=''):
        self.ledger.append(
            {"amount": -(abs(amount)), "description": description})
        return self.check_funds(amount)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        return True if self.get_balance() > amount else False

    def __str__(self):
        title = f'{self.name}'.center(30, '*')
        transactions = ''
        for item in self.ledger:
            description = item["description"][0:24]
            amount = str(item["amount"])[0:8]
            whiteSpace = (30 - len(description) - len(amount))*' '
            transactions += f'{description}{whiteSpace}{amount}\n'
        return f'{title}\n{transactions}'


def create_spend_chart(categories):
    categoriesSpentPercent = []
    longestName = ''
    for category in categories:
        longestName = category.name if len(
            longestName) < len(category.name) else longestName
        totalWithdraw = 0
        for item in category.ledger:
            if item['amount'] < 0:
                totalWithdraw += item['amount']
        categoriesSpentPercent.append(
            round(abs(totalWithdraw * 100) / (category.get_balance() - totalWithdraw)))
    percentsChart = ''
    i = 100
    while i >= 0:
        initialSpace = ''
        if 0 < i < 100:
            initialSpace = ' '
        elif i == 0:
            initialSpace = '  '
        hasSpent = ''
        for percent in categoriesSpentPercent:
            if percent >= i:
                hasSpent += ' o '
            else:
                hasSpent += '   '
        percentsChart += f'{initialSpace}{i}|{hasSpent}\n'
        i -= 10
    dashes = '-'*(len(hasSpent) + 5) + '\n'
    names = ''
    for i in range(0, len(longestName)):
        names += ' '*4
        for category in categories:
            if len(category.name) > i:
                names += f' {category.name[i]} '
            else:
                names += ' '*3
        names += '\n'
    percentsChart += dashes + names

    return percentsChart
