import pandas as pd
import project_helper

def load_data(input_path):
    """
    Load the tickers, closing price, volumes, and dividends

    Parameters
    ----------
    input_path : str
        Path to the csv file

    Returns
    -------
    high_volume_symbols : list
        The tickers within the percent top dollar
    close: DataFrame
        Close price for each ticker and date
    volume: DataFrame
        Volume for each ticker and date
    dividends: DataFrame
        Dividends for each ticker and date
    
    """
    df = pd.read_csv(input_path)
    # print(df)
    percent_top_dollar = 0.2
    high_volume_symbols = project_helper.large_dollar_volume_stocks(df, 'adj_close', 'adj_volume', percent_top_dollar)
    df = df[df['ticker'].isin(high_volume_symbols)]
    # print(df)

    close = df.reset_index().pivot(index='date', columns='ticker', values='adj_close')
    # print(close)
    volume = df.reset_index().pivot(index='date', columns='ticker', values='adj_volume')
    dividends = df.reset_index().pivot(index='date', columns='ticker', values='dividends')

    return high_volume_symbols, close, volume, dividends

