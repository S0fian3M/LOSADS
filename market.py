import random

from agent import Buyer, Seller


class Market:
    """
    A market is the place where Buyers purchases objects from Sellers.
    """

    def __init__(
            self,
            nb_trades_per_day
    ):
        """
        Instantiate the market
        :param nb_trades_per_day:
        """
        self.sellers = []
        self.buyers = []
        self.trades = []
        self.nb_trades_per_day = nb_trades_per_day

    def populate_market(
            self,
            nb_buyers: int = 0,
            nb_sellers: int = 0
    ):
        """
        Add random Buyers and Sellers to the market.
        :param nb_buyers:
        :param nb_sellers:
        :return:
        """
        if nb_sellers == 0:
            nb_sellers = random.randint(2, 2)
        if nb_buyers == 0:
            nb_buyers = random.randint(2, 2)

        for i in range(nb_sellers):
            name = f"Seller {i + 1}"
            inventory = random.randint(1, 5)
            min_price = random.randint(3, 8)
            self.sellers.append(Seller(name, inventory, min_price))

        for i in range(nb_buyers):
            name = f"Buyer {i + 1}"
            inventory = 0
            max_budget = random.randint(3, 10)
            self.buyers.append(Buyer(name, inventory, 10, max_budget))

    def record_trade(
            self,
            seller,
            buyer,
            quantity,
            price
    ):
        self.trades.append((seller, buyer, quantity, price))

    def get_active_sellers(self):
        """
        Get Sellers.
        :return: List of active Sellers.
        """
        return [seller for seller in self.sellers if seller.inventory > 0]

    def get_active_buyers(self):
        """
        Get Sellers.
        :return: List of active Buyers.
        """
        return [buyer for buyer in self.buyers if buyer.money > 0]

    def get_agents(self):
        """
        Get the list of all agents.
        :return:
        """
        return random.shuffle(self.sellers + self.buyers)

    def check_market_activity(self):
        return len(self.get_active_sellers()) > 0 and len(self.get_active_buyers()) > 0

    def run_trades(self):
        """
        Start the market economy.
        :return:
        """
        while True:
            if not self.check_market_activity():
                print("Market is inactive.")
                break
            for i in range(self.nb_trades_per_day):
                self.make_trades()

    def make_trades(self):
        """
        For each buyer, try to trade.
        :return:
        """
        for buyer in self.get_active_buyers():
            sellers = self.get_active_sellers()
            if sellers:
                seller = random.choice(sellers)
                trade_price = self.get_trade_price(buyer.max_budget, seller.min_price)

                if trade_price is not None:
                    seller.inventory -= 1
                    buyer.inventory += 1
                    seller.money += trade_price
                    buyer.money -= trade_price
                    self.record_trade(seller, buyer, 1, trade_price)

    @staticmethod
    def get_trade_price(
            buyer: Buyer,
            seller: Seller
    ):
        """
        For now, trades occur only if both price expectations are equal.
        TODO: N proposals, luck factor, complexity if items have more characteristics
        :param buyer:
        :param seller:
        :return:
        """
        # If the buyer can not afford the item, return None
        if buyer.price_expectation == seller.price_expectation:
            return buyer.price_expectation
        return None

    def print_trades(self):
        """
        Print trades history.
        :return:
        """
        for seller, buyer, quantity, price in self.trades:
            print(f"{seller.name} sold {quantity} units to {buyer.name} for {price}.")
