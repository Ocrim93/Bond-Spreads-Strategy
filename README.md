# Bond-Spreads-Strategy

# Installation 
	-- conda env create -f requirements.yml
# Statistical Arbitrage 

By looking at pairs trading for 10Y vs 5Y US Treasury bonds. The strategy exploits the stationary behavior of the spread, range bound and when there is high volatility.

Pipeline:
	1. Download the data from Yahoo Finance 
	2. Test for Stationarity
		We use the Augmented Dickey Fuller test to check our data mean reverts.
	3. Compute Spread and Feature data.
		We compute spread data, mean and Bollinger bands to understand support and resistance lines.
	4. Plot/Save bond Yields 
	5. Plot/Save Bond Spread 
	6. Plot Bond spread returns to assess stationarity of bond spread returns    



# Theory
	
	A stationary process is a stochastic process whose unconditional joint probability distribution does not change when shifted in time.
	Consequently, mean and variance does not change over time. It may have seasonal cycles around the trend line, but overall it does not trend up not down.

	Autoregressive model (AR(p)) is a representation of a type of random process. The assumption of the model is that the output variable depends linearly on its own values and on a stochastic term. Look at moving average model (MA(q)), autoregressive-moving-average model (ARMA(p,q)), autoregressive integrated moving average (ARIMA) models of time series, and GARCH(p,q)
