class Category:
    def __init__(self, desc):
        self.ledger = []
        self.desc = desc
        self.balance = 0.0

    def deposit(self, amount, desc = ''):

        if desc is not None:
            self.ledger.append(amount)
            self.ledger.append(desc)
            print(self.ledger)
            print(f'You deposited {amount} for {desc}')
        else:
            print(f'The amount of {amount} has beem added to the default deposit')
        self.balance += amount

    def withdraw(self, amount, desc = ''):
        if self.balance - amount >= 0:
            self.ledger.append(amount)
            self.ledger.append(desc)
            self.balance -= amount

            print(self.ledger)
            
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def tranfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.desc}'):
            category.desposit(amount, f'Transfer from {self.desc}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def create_spend_chart(categories):
        spend_amounts = []

        # total spent for each category
        for category in categories:
            spent = 0
            for item in category.ledger:
                if item["amount"] < 0:
                    spent += abs(item["amount"])
            spend_amounts.append(round(spent, 2))

        #calculate percentage
        total = round(sum(spend_amounts), 2)
        spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spend_amounts))

        #create the bar
        header = 'Percentage spent by category\n'
        chart = ''
        for value in reversed(range(0, 101, 10)):
            chart += str(value).rjust(3) + '|'
            for percent in spent_percentage:
                if percent >= value:
                    chart += " o "
                else:
                    chart += "   "
            chart += " \n"

        footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
        descriptions = list(map(lambda category: category.description, categories))
        max_length = max(map(lambda description: len(description), descriptions))
        descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
        for x in zip(*descriptions):
            footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

        return (header + chart + footer).rstrip("\n")


if __name__ == '__main__':
    dep = Category('')
    dep.deposit(1200, 'Food')
    print(dep.get_balance())
    print(dep.check_funds(1200))
