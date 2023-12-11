    # US Treasury Spread Tickers and Chart Labels
from Code.retrieve_web import  Yahoo_Web

bond_tickers1 = ['^IRX', '^FVX']

df = Yahoo_Web.get_prices(bond_tickers1[0], years =1 )
print(df)