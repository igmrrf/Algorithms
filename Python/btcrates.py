import sys


def Ultimate(amount, rate):
    profit = 0
    if (amount <= 100):
        profit = 3500
    elif (amount <= 500):
        profit = 3000
    elif (amount <= 1000):
        profit = 2500
    else:
        profit = 2000

    gain = (amount * profit)/100
    normal = amount * rate
    selling = (normal - gain)/amount
    print('Rate to Sell at: ',  selling)
    print("Profit: ", gain)


amount = sys.argv[1]
currentRate = sys.argv[2]

Ultimate(int(amount), int(currentRate))

# How to use
# python app.py amount rate
# replace amount and rate with


class Profits:
    def __init__(self, m, p):
        self.model = m
        self.price = p


profit = Profits(300, 400)
print(profit.model)
