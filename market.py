import random

from agent import Buyer, Seller


class Market:
    """
    A market is the place where Buyers purchases objects from Sellers.
    """

    def __init__(self):
        """
        Instantiate the market
        """
        self.sellers = []
        self.buyers = []
        self.trades = []

    def populate_market(
            self,
            nb_buyers: int,
            nb_sellers: int
    ):
        """
        Add random Buyers and Sellers to the market.
        :param nb_buyers:
        :param nb_sellers:
        :return:
        """
        for i in range(nb_buyers):
            self.buyers.append(Buyer(f"Buyer {i}", 0, random.randint(5, 50)))

        for i in range(nb_sellers):
            self.sellers.append(Seller(f"Seller {i}", random.randint(1, 20), random.randint(5, 50)))

    def record_trade(
            self,
            seller,
            buyer,
            quantity,
            price
    ):
        self.trades.append((seller, buyer, quantity, price))

    def get_sellers(self):
        """
        Get Sellers.
        :return: List of active Sellers.
        """
        return [seller for seller in self.sellers if isinstance(seller, Seller) and seller.inventory > 0]

    def get_buyers(self):
        """
        Get Sellers.
        :return: List of active Buyers.
        """
        return [buyer for buyer in self.buyers if isinstance(buyer, Buyer) and buyer.inventory > 0 and buyer.budget > 0]

    def get_agents(self):
        """
        Get the list of all agents.
        :return:
        """
        return [self.sellers, self.buyers]

    def check_market_activity(self):
        for buyer in self.buyers:
            if buyer.inventory > 0 and buyer.budget > 0:
                return True

        for seller in self.sellers:
            if seller.inventory > 0 and seller.budget > 0:
                return True
        return False

    def run_trades(self):
        """
        Start the market economy.
        :return:
        """
        while True:
            if not self.check_market_actvity():
                print("Market is inactive.")
                break

            for seller in self.sellers:
                seller.make_trade(self)

            for buyer in self.buyers:
                buyer.make_trade(self)

    def print_trades(self):
        """
        Print trades history.
        :return:
        """
        for seller, buyer, quantity, price in self.trades:
            print(f"{seller.name} sold {quantity} units to {buyer.name} for {price}.")
