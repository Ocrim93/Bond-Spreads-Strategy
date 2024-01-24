# Bond-Spreads-Strategy

# Installation 
	-- conda env create -f requirements.yml
# Statistical Arbitrage 

By looking at pairs trading for 10Y vs 5Y US Treasury bonds. The strategy exploits the stationary behavior of the spread, range bound and when there is high volatility.\
Pipeline:
##
<ol>
	<li>Download the data from Yahoo Finance</li>
	<li>Test for Stationarity
		<ul>
			<li>We use the Augmented Dickey Fuller test to check our data mean reverts</li>
		</ul>
	</li>
	<li>Compute Spread and Feature data.
		<ul>
			<li>We compute spread data, mean and Bollinger bands to understand support and resistance lines.</li>
		</ul>
	</li>
	<li>Plot/Save bond Yields</li>
	<li>Plot/Save Bond Spread </li>
	<li>Plot Bond spread returns to assess stationarity of bond spread returns</li>
</ol>

# Theory
	
A stationary process is a stochastic process whose unconditional joint probability distribution does not change when shifted in time.\
Consequently, mean and variance does not change over time. It may have seasonal cycles around the trend line, but overall it does not trend up not down.\

Autoregressive model (AR(p)) is a representation of a type of random process. The assumption of the model is that the output variable depends linearly on its own values and on a stochastic term. Look at moving average model (MA(q)), autoregressive-moving-average model (ARMA(p,q)), autoregressive integrated moving average (ARIMA) models of time series, and GARCH(p,q)
