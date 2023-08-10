[![Github commit](https://img.shields.io/github/last-commit/QI2lab/mcSIM)](https://github.com/fdjutant/portfolio-optimization)

# Building and optimizing smart beta portfolio
## Project overview
Smart beta portfolio allows a passive approach in discovering the most optimal portfolio weights. The strategy used here is 
to determine the portfolio weights based on the total dividend yield over time. A comparison of cumulative returns from this strategy is then compared with that of exchanged traded fund (ETF) to evalute the strategy effectiveness.

To evaluate the strategy, a synthetic data consisting of price data, ETF index weights, and dividends are spanning across four years time frame with a total of 99 indices.

## Project description
# Smart beta portfolio
The following steps were taken to generate portfolio weights that outperforms ETF. First, the time-series index weights based on the large dollar volume stocks were computed using the closing price and volume. Second, the time-series index weights based on dividends were computed using the dividend data. Third, the weighted returns for both the beta portfolio and ETF were calculated from the time-series price data and their corresponding weights. Finally, the resulting difference between the smart beta strategy and an ETF can be shown by comparing their cumulative returns over the course of four years time frame.

To evaluate the performace of the smart beta portfolio tracking the ETF returns, an annualized tracking error can be computed by taking a standard deviation of the difference between the portfolio returns and the benchmark returns.

## Portfolio optimization
Here, a simple portfolio optimization was performed by minimizing the quantity of the portfolio variance and the discrepancy between the portfolio weights and a market cap weighted index.

The portfolio variance was quantified by computing its covariance matrix. On the other hand, how closely the smart beta portfolio weights following the benchmark index was simply calculated by taking an L2 norm. The objective function constructed from these two factors, and they are scaled by &#03BB;. To ensure that the index weight optimization is applicable for a smart beta portfolio, that is long only, the following constraints are added: the weights must be positive and its sum is equal to one.

Finally, the portfolio turnover was also computed to estimate the cost of rebalancing the portfolio. This was simply computed by multiplying the ratio of number of rebalance annually to number of rebalance events with the sum of total turnover. The sum of total turnover is simply estimated by summing the absolute difference of portolio weights across time and indices.

## Credits
The project was built as a part of a practical course in systematic trading from Udacity: [AI for trading](https://www.udacity.com/course/ai-for-trading--nd880)