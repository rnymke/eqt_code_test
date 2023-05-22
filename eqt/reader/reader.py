import pandas as pd
from reader.utils.utils import url_to_soup


def read_funds(url):
    return _funds_to_pdf_df(url_to_soup(url))

def read_portfolio(url):
    return _div_or_port_to_pdf(url_to_soup(url))

def read_divestments(url):
    return _div_or_port_to_pdf(url_to_soup(url))

def _funds_to_pdf_df(funds_soup):
    fund_list = []
    for fund in funds_soup:
        fund_name = fund.find('span', {'class': 'inline-block'}).get_text()

        fund_info = fund.find_all('span', {'class': 'flex-1 font-light'})
        fund_launch = fund_info[0].get_text()
        fund_size = fund_info[1].get_text()
        fund_status = fund_info[2].get_text()
        fund_sfdr = fund_info[3].get_text()

        fund_list.append([fund_name, fund_launch, fund_size, fund_status, fund_sfdr])
    return pd.DataFrame(fund_list, columns=["fund", "launch", "size", "status", "sfdr"])


def _div_or_port_to_pdf(soup):
    """
    Given divestments or portfolio soup, transforms html to pandas dataframe
    containing ["company", "sector", "country", "funds", "entry", "exit"]

    TODO: Should add content from EQT-URL when available
    :param soup:
    :return:
    """
    elem_list = []
    for elem in soup:
        company = elem.find("span", {
            "class": "relative inline-flex items-center pb-2 transition-hover font-t-bold text-t-400 text-secondary-darker"}).get_text()

        elem_info = elem.find("div", {"class": "h-0 overflow-hidden transition-all duration-200"}).find_all("span", {
            "class": "flex-1 font-light"})
        sector = elem_info[0].get_text()
        country = elem_info[1].get_text()
        funds = ','.join([fund_name.get_text() for fund_name in elem_info[2].find_all("li")])
        entry = elem_info[3].get_text()
        exit = elem_info[4].get_text() if len(elem_info) > 4 else None

        elem_list.append([company, sector, country, funds, entry, exit])

    return pd.DataFrame(elem_list, columns=["company", "sector", "country", "funds", "entry", "exit"])