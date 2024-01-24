# US Treasury Spread Tickers and Chart Labels
from Code.web_requests import  Yahoo_Web
from Code.spread import Bond_Spread
from Code import utilities

utilities.create_folder()

#label1 = '5Y - 2Y'
bond_tickers = ['^IRX', '^FVX']

spread = Bond_Spread(
				 long_duration_bond  = bond_tickers[0],
				 short_duration_bond= bond_tickers[1],
				 years = 3)

spread.compute_spread()
spread.apply_trading_indicator('EMA', 20)
print(spread.data)



# US Treasury Spread Tickers and Chart Labels
#label1 = '5Y - 2Y'
#bond_tickers1 = {'^IRX', '^FVX'}
#label2 = '10Y - 2Y'
#bond_tickers2 = {'^TNX', '^IRX'}
#label3 = '10Y - 5Y'
#bond_tickers3 = {'^TNX', '^FVX'}
    