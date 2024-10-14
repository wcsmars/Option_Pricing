import numpy as np
from scipy.stats import norm

def black_scholes_merton(call_option, spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation):
    d1 = (np.log(spot_price / strike_price) + (risk_free_rate - dividend_yield + 0.5 * standard_deviation**2) * time_to_maturity) / (standard_deviation * np.sqrt(time_to_maturity))
    d2 = d1 - standard_deviation * np.sqrt(time_to_maturity)
    
    if call_option:
        option_price = spot_price * np.exp(-dividend_yield * time_to_maturity) * norm.cdf(d1) - strike_price * np.exp(-risk_free_rate * time_to_maturity) * norm.cdf(d2)
    else:
        option_price = strike_price * np.exp(-risk_free_rate * time_to_maturity) * norm.cdf(-d2) - spot_price * np.exp(-dividend_yield * time_to_maturity) * norm.cdf(-d1)
    
    return option_price

call_option = input(("Call option (T / F): ")) == "T"
spot_price = float(input("Enter the spot price of the underlying asset: "))
strike_price = float(input("Enter the strike price of the option: "))
risk_free_rate = float(input("Enter the risk-free rate (as a decimal): "))
dividend_yield = float(input("Enter the dividend yield (as a decimal, enter 0 if none): "))
time_to_maturity = float(input("Enter the time to maturity in years: "))
standard_deviation = float(input("Enter the standard deviation of the underlying asset (as a decimal): "))

print(black_scholes_merton(call_option, spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation))
