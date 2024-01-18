# US Treasury Spread Tickers and Chart Labels
from Code.retrieve_web import  Yahoo_Web
from Code import spreadr
from Code import utilities

utilities.create_folder()

#label1 = '5Y - 2Y'
bond_tickers = ['^IRX', '^FVX']

df = Yahoo_Web.get_prices(bond_tickers, years =1 )

label = "{} - {}".format(bond_tickers[1],bond_tickers[0])
adj_df = df.copy()['Adj Close']
spread.compute_spread(adj_df,label)




# US Treasury Spread Tickers and Chart Labels
#label1 = '5Y - 2Y'
#bond_tickers1 = {'^IRX', '^FVX'}
#label2 = '10Y - 2Y'
#bond_tickers2 = {'^TNX', '^IRX'}
#label3 = '10Y - 5Y'
#bond_tickers3 = {'^TNX', '^FVX'}
    