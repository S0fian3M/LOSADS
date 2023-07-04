import random


class Agent:
    """
    Agent class interface.
    """

    def __init__(
            self,
            name: str,
            inventory: int
    ):
        """
        Instantiate the agent.
        :param name: String. Agent's name.
        :param inventory: Inventory of objects.
        """
        self.name = name
        self.inventory = inventory


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
            money,
            min_price,
            price_expectation
    ):
        super().__init__(name, inventory)
        self.money = money
        self.min_price = min_price
        self.price_expectation = price_expectation


class Buyer(Agent):
    """
    A Buyer refers to an agent with the goal of buying objects.
    """

    def __init__(
            self,
            name,
            inventory,
            money,
            max_budget,
            price_expectation
    ):
        super().__init__(name, inventory)
        self.money = money
        self.max_budget = max_budget
        self.price_expectation = price_expectation
