import numpy as np

def binomial_tree_pricer(European_or_American, option_type, spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation, number_of_period):

    dt = time_to_maturity / number_of_period
    u = np.exp(standard_deviation * np.sqrt(dt))
    d = 1 / u
    p = (np.exp((risk_free_rate - dividend_yield) * dt) - d) / (u - d)
    discount = np.exp(-risk_free_rate * dt)
    
    # Initialize the asset prices at maturity
    asset_prices = np.zeros(number_of_period + 1)
    option_values = np.zeros(number_of_period + 1)
    
    for j in range(number_of_period + 1):
        asset_prices[j] = spot_price * (u ** (number_of_period - j)) * (d ** j)
    
    # Calculate option values at maturity
    if option_type == 'C':
        for j in range(number_of_period + 1):
            option_values[j] = max(0, asset_prices[j] - strike_price)
    elif option_type == 'P':
        for j in range(number_of_period + 1):
            option_values[j] = max(0, strike_price - asset_prices[j])
    
    # Work backwards through the tree
    for i in range(number_of_period - 1, -1, -1):
        for j in range(i + 1):
            option_values[j] = (p * option_values[j] + (1 - p) * option_values[j + 1]) * discount
            asset_price = spot_price * (u ** (i - j)) * (d ** j)
            if European_or_American == 'A':
                if option_type == 'C':
                    option_values[j] = max(option_values[j], asset_price - strike_price)
                elif option_type == 'P':
                    option_values[j] = max(option_values[j], strike_price - asset_price)
    
    return option_values[0]

if __name__ == '__main__':
    European_or_American = input("European or American option (E / A): ").upper()
    while European_or_American not in ['E', 'A']:
        European_or_American = input("Invalid input. Please enter 'E' for European or 'A' for American: ").upper()

    option_type = input("Call or Put option (C / P): ").upper()
    while option_type not in ['C', 'P']:
        option_type = input("Invalid input. Please enter 'C' for Call or 'P' for Put: ").upper()

    try:
        spot_price = float(input("Enter the spot price of the underlying asset: "))
        strike_price = float(input("Enter the strike price of the option: "))
        risk_free_rate = float(input("Enter the risk-free rate (as a decimal): "))
        dividend_yield = float(input("Enter the dividend yield (as a decimal, enter 0 if none): "))
        time_to_maturity = float(input("Enter the time to maturity in years: "))
        standard_deviation = float(input("Enter the standard deviation of the underlying asset (as a decimal): "))
        number_of_period = int(input("Enter the number of periods: "))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

    option_price = binomial_tree_pricer(European_or_American, option_type, spot_price, strike_price, risk_free_rate, dividend_yield, time_to_maturity, standard_deviation, number_of_period)
    print(f"The price of the {'call' if option_type == 'C' else 'put'} option is: ${option_price:}")
