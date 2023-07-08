import matplotlib.pyplot as plt


class MarketVisualizer:
    """
    Visualize the market
    """

    def __init__(
            self,
            market
    ):
        self.market = market

    def visualize_market_activity(self):
        """
        Real-time plot of active agents
        :return:
        """
        active_sellers = len(self.market.get_active_sellers())
        active_buyers = len(self.market.get_active_buyers())

        labels = ['Active Sellers', 'Active Buyers']
        values = [active_sellers, active_buyers]

        plt.bar(labels, values)
        plt.xlabel('Agent Type')
        plt.ylabel('Number of Agents')
        plt.title('Market Activity')
        plt.show()

    def visualize_price_trends(self):
        """
        Plot price expectations
        :return:
        """
        # Get price expectations of sellers and buyers
        seller_prices = [seller.price_expectation for seller in self.market.sellers]
        buyer_prices = [buyer.price_expectation for buyer in self.market.buyers]

        # Plot price trends
        plt.plot(range(len(seller_prices)), seller_prices, label='Seller Price Expectation')
        plt.plot(range(len(buyer_prices)), buyer_prices, label='Buyer Price Expectation')

        plt.xlabel('Time')
        plt.ylabel('Price Expectation')
        plt.title('Price Trends')
        plt.legend()
        plt.show()
