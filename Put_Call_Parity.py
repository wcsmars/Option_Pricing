from Black_Scholes_Merton import black_scholes_merton
from Binomial_Tree import binomial_tree_pricer
import numpy as np 
from scipy.stats import norm

def put_call_parity(pricing_model, spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation, number_of_period = None):
    if pricing_model == 'BSM':
        call_price = black_scholes_merton('C', spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation)
        put_price = black_scholes_merton('P', spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation)
    elif pricing_model == 'BT':
        if number_of_period is None:
            raise ValueError("Number of periods must be specified for Binomial Tree model.")
        call_price = binomial_tree_pricer('E', 'C', spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation, number_of_period)
        put_price = binomial_tree_pricer('E', 'P', spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation, number_of_period)
    else:
        raise ValueError("Invalid pricing model. Choose 'BSM' or 'BT'.")
    
    lhs = call_price - put_price
    rhs = spot_price * np.exp(-dividend_yield * time_to_maturity) - strike_price * np.exp(-risk_free_rate * time_to_maturity)

    return np.isclose(lhs, rhs), lhs, rhs

try:
    spot_price = float(input("Enter the spot price of the underlying asset: "))
    strike_price = float(input("Enter the strike price of the option: "))
    risk_free_rate = float(input("Enter the risk-free rate (as a decimal): "))
    dividend_yield = float(input("Enter the dividend yield (as a decimal, enter 0 if none): "))
    time_to_maturity = float(input("Enter the time to maturity in years: "))
    standard_deviation = float(input("Enter the standard deviation of the underlying asset (as a decimal): "))
except ValueError:
    print("Invalid input. Please enter numerical values.")
    exit()

pricing_model = input("Select pricing model ('BSM' for Black-Scholes-Merton or 'BT' for Binomial Tree): ").upper()
while pricing_model not in ['BSM', 'BT']:
    pricing_model = input("Invalid input. Please enter 'BSM' or 'BT': ").upper()

if pricing_model == 'BT':
    try:
        number_of_period = int(input("Enter the number of periods for the Binomial Tree model: "))
    except ValueError:
        print("Invalid input. Please enter an integer value for number of periods.")
        exit()
else:
    number_of_period = None

parity_holds, lhs, rhs = put_call_parity(
    pricing_model,
    spot_price,
    strike_price,
    risk_free_rate,
    dividend_yield,
    time_to_maturity,
    standard_deviation,
    number_of_period
)
print(f"LHS (Call - Put): {lhs}")
print(f"RHS (S * exp(-q * T) - K * exp(-r * T)): {rhs}")
print(f"Put-Call Parity holds: {parity_holds}")
