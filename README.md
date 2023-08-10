[![Github commit](https://img.shields.io/github/last-commit/fdjutant/portfolio-optimization/master)](https://github.com/fdjutant/portfolio-optimization)

# Building and optimizing smart beta portfolio
## Project overview
A smart beta portfolio is an investment portfolio that follows an underlying index and is optimized using the same techniques that active portfolio managers utilize. It allows a passive approach to discover the most optimal investment opportunities and combines it with the active involvement of skilled managers. The strategy used here is to determine the portfolio weights based on the total dividend yield over time. A comparison of cumulative returns from this strategy is then made with that of an exchange-traded fund (ETF) to evaluate the strategy effectiveness.

To evaluate the strategy, a synthetic data set consisting of price data, ETF index weights, and dividends spanning across four years time frame with a total of 99 indices is used.

## Project description
### Smart beta portfolio
The following steps were taken to generate portfolio weights that outperform the ETF. First, the time-series index weights based on the large dollar volume stocks were computed using the closing price and volume. Second, the time-series index weights based on dividends were computed using the dividend data. Third, the weighted returns for both the beta portfolio and the ETF were calculated from the time-series price data and their corresponding weights. Finally, the resulting difference between the smart beta strategy and the ETF can be shown by comparing their cumulative returns over the course of four years time frame.

To evaluate the performance of the smart beta portfolio tracking the ETF returns, an annualized tracking error can be computed by taking the standard deviation of the difference between the portfolio returns and the benchmark returns.

![Alt text](./graphs/smart-beta-vs-ETF.png?raw=true "Cumulative returns of smart beta vs ETF")


### Portfolio optimization
In this project, a simple portfolio optimization was performed by minimizing the combination of the portfolio variance and the deviation between the portfolio weights and a market cap weighted index.

The portfolio variance was quantified by computing its covariance matrix, which measures the degree of correlation among the returns of different assets in the portfolio. On the other hand, the deviation between the smart beta portfolio weights and the benchmark index weights was calculated by taking an L2 norm, which is the square root of the sum of squared differences. The objective function was constructed from these two factors, and they were scaled by a parameter &#955; that represents the trade-off between minimizing variance and tracking the index. To ensure that the index weight optimization is applicable for a smart beta portfolio, which is long only, the following constraints were added: the weights must be positive and their sum must be equal to one.

![Alt text](./graphs/optimized-smart-beta-vs-ETF.png?raw=true "Cumulative returns of optimized smart beta vs ETF")

Finally, the portfolio turnover was also computed to estimate the cost of rebalancing the portfolio. This was simply computed by multiplying the ratio of the number of rebalances annually to the number of rebalance events with the sum of total turnover. The sum of total turnover was estimated by summing the absolute difference of portfolio weights across time and indices.


## Credits
The project was built as part of a practical course in systematic trading from Udacity: [AI for trading](https://www.udacity.com/course/ai-for-trading--nd880)