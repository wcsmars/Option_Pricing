from Black_Scholes_Merton import black_scholes_merton
import numpy as np 
from scipy.stats import norm

def put_call_parity(spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation):
    call_price = black_scholes_merton(True, spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation)
    put_price = black_scholes_merton(False, spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation)

    lhs = call_price - put_price
    rhs = spot_price * np.exp(-dividend_yield * time_to_maturity) - strike_price * np.exp(-risk_free_rate * time_to_maturity)

    return np.isclose(lhs, rhs), lhs, rhs

spot_price = float(input("Enter the spot price of the underlying asset: "))
strike_price = float(input("Enter the strike price of the option: "))
risk_free_rate = float(input("Enter the risk-free rate (as a decimal): "))
dividend_yield = float(input("Enter the dividend yield (as a decimal, enter 0 if none): "))
time_to_maturity = float(input("Enter the time to maturity in years: "))
standard_deviation = float(input("Enter the standard deviation of the underlying asset (as a decimal): "))

parity_holds, lhs, rhs = put_call_parity(spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation)

print(f"LHS (Call - Put): {lhs}")
print(f"RHS (S * exp(-q * T) - K * exp(-r * T)): {rhs}")
print(f"Put-Call Parity holds: {parity_holds}")
