import numpy as np

def get_covariance_returns(returns):
    """
    Calculate covariance matrices.

    Parameters
    ----------
    returns : DataFrame
        Returns for each ticker and date

    Returns
    -------
    returns_covariance  : 2 dimensional Ndarray
        The covariance of the returns
    """
    #TODO: Implement function

    returns_covariance = np.cov(returns. fillna(0).transpose())
    
    return returns_covariance

import cvxpy as cvx

def get_optimal_weights(covariance_returns, index_weights, scale=2.0):
    """
    Find the optimal weights.

    Parameters
    ----------
    covariance_returns : 2 dimensional Ndarray
        The covariance of the returns
    index_weights : Pandas Series
        Index weights for all tickers at a period in time
    scale : int
        The penalty factor for weights the deviate from the index 
    Returns
    -------
    x : 1 dimensional Ndarray
        The solution for x
    """
    assert len(covariance_returns.shape) == 2
    assert len(index_weights.shape) == 1
    assert covariance_returns.shape[0] == covariance_returns.shape[1]  == index_weights.shape[0]

    #TODO: Implement function
    print(index_weights)
    
    # index weight variable
    x = cvx.Variable(len(index_weights))
    
    # difference with index and volatility
    distance_to_index = cvx.norm(x-index_weights, p=2, axis=None)
    volatility = cvx.quad_form(x, covariance_returns)
    
    # objective function
    objective = cvx.Minimize(volatility + scale * distance_to_index)
    constraints = [x >= 0, sum(x)==1]
    problem = cvx.Problem(objective, constraints)
    min_value = problem.solve()
    x_values = x.value
    print(x_values)
    
    return x_values