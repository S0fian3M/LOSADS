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
            num_sellers = random.randint(2, 2)
        if nb_buyers == 0:
            num_buyers = random.randint(2, 2)

        for i in range(num_sellers):
            name = f"Seller {i + 1}"
            inventory = random.randint(1, 5)
            min_price = random.randint(3, 8)
            self.sellers.append(Seller(name, inventory, min_price))

        for i in range(num_buyers):
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

            self.make_trades()

    def make_trades(self):
        """
        Make all trades.
        :return:
        """
        for seller in self.get_active_sellers():
            buyers = self.get_active_buyers()
            if buyers:
                buyer = random.choice(buyers)
                total_cost = self.get_trade_price(buyer.max_budget, seller.min_price)

                seller.inventory -= 1
                buyer.inventory += 1
                buyer.max_budget -= total_cost
                self.record_trade(seller, buyer, 1, total_cost)

    @staticmethod
    def get_trade_price(
            proposal_1: int,
            proposal_2: int
    ):
        """
        For now, the trade price will be the minimum of 2 proposals.
        TODO: N proposals, luck factor, complexity if items have more characteristics
        :param proposal_1:
        :param proposal_2:
        :return:
        """
        return min(proposal_1, proposal_2)

    def print_trades(self):
        """
        Print trades history.
        :return:
        """
        for seller, buyer, quantity, price in self.trades:
            print(f"{seller.name} sold {quantity} units to {buyer.name} for {price}.")
