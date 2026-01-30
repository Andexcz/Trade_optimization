import numpy as np

def kelly_analysis(mu, sigma):
    Optimal_leverage= mu / (sigma ** 2)
    RA_return=mu-(Optimal_leverage*(sigma**2))/2
    print(f"Optimal leverage: {Optimal_leverage}")
    print(f"Risk-adjusted return at optimal leverage: {RA_return}")
# Example usage
kelly_analysis(0.08,0.2)    