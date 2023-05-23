import pandas as pd

def restructure_test_funding(test_funding_raw):
    """
    Restructures test_funding json to pandas dataframe, returns [company_name, funding]
    where funding is a list of dicts containing the columns from test_funding_raw.
    This is done by grouping by company_name and collecting each row as a separate dict entry.

    :param test_funding_raw: test_funding_raw as pandas df
    :return: restructured pandas dataframe, [company_name, funding] where funding is a dict
    """
    df = test_funding_raw.copy() # TODO: Double check if this copy needs to be explicit
    df['index'] = df.index
    df['funding']=df[[col for col in test_funding_raw.columns if col not in ["index", "company_name", "funding"]]].to_dict("records")
    df = df[['company_name','funding']]
    df = df.groupby('company_name')['funding'].apply(list)
    df = pd.DataFrame.from_dict(df)
    df.reset_index() # TODO: can likely make joins more effective by using indices properly
    return df

def rename_divestments(divestments):
    """
    Renames entry, exit and funds to previous_*, where * in [entry, exit, funds]
    :param divestments: pandas df of divestments
    :return: divestments, but with renamed columns
    """
    return divestments.rename(columns={"entry": "previous_entry", "exit": "previous_exit", "funds": "previous_funds"})