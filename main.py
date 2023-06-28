import random

from market import Market
from agent import Seller, Buyer

def main():
    market = Market()
    market.populate_market()

    market.run_trades()
    market.print_trades()

    for agent in market.sellers + market.buyers:
        print(f"{agent}: {agent.inventory} units")


if __name__ == "__main__":
    main()