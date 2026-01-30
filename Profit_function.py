import numpy as np

#Profit function: P(x) = αx - βx² - cx
#Arguments: 
# α - expected return per share
# β - market impact coefficient (for example, price slippage due to low liquidity)
# c - transaction cost per share
# x - number of shares to trade

def profit_analysis(alpha, beta, c):
    # Calculate the optimal number of shares to trade
    x_optimal = (alpha - c) / (2 * beta)
    print(f"Optimal number of shares to trade: {x_optimal}")
    # Calculate the maximum profit at the optimal number of shares
    max_profit = alpha * x_optimal - beta * x_optimal**2 - c * x_optimal
    print(f"Maximum profit at optimal trade: {max_profit}")
    return x_optimal, max_profit
# Example usage
profit_analysis(0.05,0.0001,0.01)

# The second derivative of the profit function P''(x) = -2β
# This confirms that the profit function is concave down, indicating a maximum at the optimal point.
def second_derivative_test(beta):
    second_derivative = -2 * beta
    if second_derivative < 0:
        print("The profit function is concave down at the optimal point, confirming a maximum.")
    else:
        print("The profit function is not concave down at the optimal point.")
    return second_derivative
# Example usage
second_derivative_test(0.0001)