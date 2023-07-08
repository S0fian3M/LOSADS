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
            self.sellers.append(Seller(name, inventory, 0, min_price, min_price + random.randint(1, 5)))

        for i in range(nb_buyers):
            name = f"Buyer {i + 1}"
            inventory = 0
            max_budget = random.randint(3, 10)
            self.buyers.append(Buyer(name, inventory, 10, max_budget, max_budget + random.randint(1, 5)))

    def record_trade(
            self,
            seller,
            buyer,
            quantity,
            price
    ):
        """
        Record a trade between two agents
        :param seller:
        :param buyer:
        :param quantity:
        :param price:
        :return:
        """
        self.trades.append((seller, buyer, quantity, price))

    def get_active_sellers(self):
        """
        Get Sellers.
        :return: List of active Sellers.
        """
        return [seller for seller in self.sellers if seller.inventory > 0 and seller.has_recently_sold is True]

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
        """
        Check whether some agents are still active
        :return:
        """
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
            # Do all trades during a day
            for i in range(self.nb_trades_per_day):
                self.make_trades()
            self.update_price_expectations()

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
                    seller.money += trade_price
                    seller.has_recently_sold = True

                    buyer.inventory += 1
                    buyer.money -= trade_price
                    buyer.has_recently_bought = True

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

    def update_price_expectations(self):
        """
        All agents update their price expectations at the end of the day
        :return:
        """
        for buyer in self.buyers:
            if buyer.has_recently_bought:
                buyer.price_expectation += 1
            else:
                buyer.price_expectation = min(1, buyer.price_expectation - 1)

        for seller in self.sellers:
            if seller.has_recently_sold:
                seller.price_expectation += 1
            else:
                seller.price_expectation = min(1, seller.price_expectation - 1)

    def print_trades(self):
        """
        Print trades history.
        :return:
        """
        for seller, buyer, quantity, price in self.trades:
            print(f"{seller.name} sold {quantity} units to {buyer.name} for {price}.")
