import smart_beta
import portfolio_optimization
import pandas as pd
import numpy as np

import helper
import project_helper
import project_tests
import misc

if __name__ == "__main__":

    # load the data from the csv file
    high_volume_symbols, close, volume, dividends = misc.load_data('./data/eod-quotemedia.csv')
    
    # generate the weights based on dollar volume traded for that date
    # project_tests.test_generate_dollar_volume_weights(smart_beta.generate_dollar_volume_weights)
    index_weights = smart_beta.generate_dollar_volume_weights(close, volume)
    project_helper.plot_weights(index_weights, 'Index Weights')

    # generate the ETF weights and plot it using a heatmap
    etf_weights = smart_beta.calculate_dividend_weights(dividends)
    project_helper.plot_weights(etf_weights, 'ETF Weights')
    
    # generate returns and plot it with a heatmap
    returns = smart_beta.generate_returns(close)
    project_helper.plot_returns(returns, 'Close Returns')

    # generate the ETF and index returns, then view them using a heatmap.
    index_weighted_returns = smart_beta.generate_weighted_returns(returns, index_weights)
    etf_weighted_returns = smart_beta.generate_weighted_returns(returns, etf_weights)
    project_helper.plot_returns(index_weighted_returns, 'Index Returns')
    project_helper.plot_returns(etf_weighted_returns, 'ETF Returns')

    # generate the ETF and index cumulative returns, then compare the trajectory
    index_weighted_cumulative_returns = smart_beta.calculate_cumulative_returns(index_weighted_returns)
    etf_weighted_cumulative_returns = smart_beta.calculate_cumulative_returns(etf_weighted_returns)
    project_helper.plot_benchmark_returns(index_weighted_cumulative_returns, etf_weighted_cumulative_returns, 'Smart Beta ETF vs Index')

    # compute the tracking error between the ETF and index
    smart_beta_tracking_error = smart_beta.tracking_error(np.sum(index_weighted_returns, 1), np.sum(etf_weighted_returns, 1))
    print('Smart Beta Tracking Error: {}'.format(smart_beta_tracking_error))
    
    # compute covariance and view the data
    covariance_returns = portfolio_optimization.get_covariance_returns(returns)
    covariance_returns = pd.DataFrame(covariance_returns, returns.columns, returns.columns)

    covariance_returns_correlation = np.linalg.inv(np.diag(np.sqrt(np.diag(covariance_returns))))
    covariance_returns_correlation = pd.DataFrame(
        covariance_returns_correlation.dot(covariance_returns).dot(covariance_returns_correlation),
        covariance_returns.index,
        covariance_returns.columns)

    project_helper.plot_covariance_returns_correlation(
        covariance_returns_correlation,
        'Covariance Returns Correlation Matrix')
    
    # optimize the portfolio weights by using the covariance information
    raw_optimal_single_rebalance_etf_weights = portfolio_optimization.get_optimal_weights(covariance_returns.values, index_weights.iloc[-1])
    optimal_single_rebalance_etf_weights = pd.DataFrame(
        np.tile(raw_optimal_single_rebalance_etf_weights, (len(returns.index), 1)),
        returns.index,
        returns.columns)