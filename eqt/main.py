import pandas as pd
from pathlib import Path
from reader.reader import read_funds, read_portfolio, read_divestments
from writer.writer import write_local
from transformer.transformer import restructure_test_funding, rename_divestments

### TODO: Should be in config and/or argparser
# URLs
funds_url = "https://eqtgroup.com/current-portfolio/funds/"
portfolio_url = "https://eqtgroup.com/current-portfolio/"
divestments_url = "https://eqtgroup.com/current-portfolio/divestments/"

# Paths
base_data_path = Path(__file__).parent.parent
interview_test_funding_path = base_data_path / "data/interview-test-funding.json.gz"
interview_test_org_path = base_data_path / "data/interview-test-org.json.gz"

output_path = "./merged.json"



if __name__ == '__main__':

    # Webscrape EQT-data
    funds = read_funds(funds_url)
    portfolios = read_portfolio(portfolio_url)
    divestments = read_divestments(divestments_url)

    # Read externally provided .json's
    test_funding_raw = pd.read_json(interview_test_funding_path, lines=True)
    test_org_raw = pd.read_json(interview_test_org_path, lines=True)

    ## Transformations
    # Restructure test_funding, grouping each funding run and collecting it in a list for each company
    test_funding_restructured = restructure_test_funding(test_funding_raw)
    renamed_divestments = rename_divestments(divestments)

    ## Merge dataframes
    internal_merged = portfolios.merge(renamed_divestments[["company", "previous_funds", "previous_entry", "previous_exit"]],
                            on='company', how="outer")

    external_merged = test_org_raw.merge(test_funding_restructured, on="company_name", how="left")
    external_merged = external_merged.rename(columns={"company_name": "company"})

    merged = internal_merged.merge(external_merged, on="company", how="left")

    write_local(merged, output_path)