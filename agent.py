import random


class Agent:
    """
    Agent class interface.
    """

    def __init__(
            self,
            name: str,
            inventory
    ):
        """
        Instantiate the agent.
        :param name: String. Agent's name.
        :param inventory: Inventory of objects.
        """
        self.name = name
        self.inventory = inventory

    def make_trade(
            self,
            market
    ):
        """
        When the agent trades.
        :param market:
        :return:
        """
        pass

    def __str__(self):
        return f"{self.name}: {self.inventory}"


class Seller(Agent):
    """
    A Seller refers to an agent with the goal of selling objects.
    """

    def __init__(
            self,
            name,
            inventory,
            min_price
    ):
        super().__init__(name, inventory)
        self.min_price = min_price

    def make_trade(
            self,
            market
    ):
        if self.inventory > 0:
            buyers = market.get_buyers()
            if buyers:
                buyer = random.choice(buyers)
                quantity = min(self.inventory, buyer.inventory)
                total_cost = self.min_price * quantity

                self.inventory -= quantity
                buyer.inventory -= quantity
                market.record_trade(self, buyer, quantity, total_cost)


class Buyer(Agent):
    """
    A Buyer refers to an agent with the goal of buying objects.
    """

    def __init__(
            self,
            name,
            inventory,
            max_budget
    ):
        super().__init__(name, inventory)
        self.max_budget = max_budget

    def make_trade(
            self,
            market
    ):
        if self.inventory > 0 and self.max_budget > 0:
            sellers = market.get_sellers()
            if sellers:
                seller = random.choice(sellers)
                quantity = min(self.inventory, seller.inventory)
                total_cost = seller.price * quantity

                if self.max_budget >= total_cost:
                    self.inventory -= quantity
                    self.max_budget -= total_cost
                    market.record_trade(seller, self, quantity, total_cost)
