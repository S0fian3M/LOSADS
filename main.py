from market import Market


def main():
    """
    Start the market simulation
    :return:
    """
    market = Market(10)
    market.populate_market()

    market.run_trades()
    market.print_trades()

    for agent in market.sellers + market.buyers:
        print(f"{agent}: {agent.inventory} units")


if __name__ == "__main__":
    main()
