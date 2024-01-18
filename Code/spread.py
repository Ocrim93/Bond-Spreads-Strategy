import pandas as pd
from statsmodels.tsa.stattools import adfuller
from .plotting_lib import plot

def stationary_test(data, threshold = 0.05):
	"""
    Perform Augmented Dickey-Fuller test for stationarity.
    """
	test = adfuller(data, autolag='AIC')
	print(test)
	p_value = test[1]
	is_stationary = p_value < threshold

	msg = "*** STATIONARY ***" if is_stationary else "not stationary"
	print(f'Series is {msg} (p-value: {p_value:.4f})')
	return p_value


def compute_spread(prices : pd.DataFrame(), label : str, ):
	#Compute the spread as differences between two series 

	prices['spread'] = prices.iloc[:,1] - prices.iloc[:,0]

	#Compute Average Spread 
	avg_spread = prices['spread'].mean()
	print(f"Average {label}: {avg_spread:.2f}")
	stationary_test(prices['spread'])
	plot(prices, label, 'Date','spread', label,average = avg_spread)

