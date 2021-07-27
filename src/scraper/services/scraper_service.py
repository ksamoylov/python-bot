import mechanicalsoup
from src.helpers.environment_helper import get_env_by_name
from src.etf.entity.Etf import Etf


def scrap_page(uri: str):
    soup = get_soup(uri)
    get_fields_from_soup(soup)


def get_soup(uri: str):
    browser = mechanicalsoup.Browser()
    page = browser.get(uri)

    return page.soup


def get_fields_from_soup(soup):
    etf = create_etf(soup.select(".field_scroll_1")[0])
    print(etf.get_fund_comp_name())


def create_etf(etf_element) -> Etf:
    return Etf(**{
        'latest_quotation_date': etf_element.select(".field_latest_quotation_date")[0].text.strip(),
        'fund_comp_name': etf_element.select(".field_fund_comp_name")[0].text.strip(),
        'currency_name': etf_element.select(".field_etf_currency_name")[0].text.strip(),
        'close': etf_element.select(".field_close")[0].text.strip(),
        'change_one_day': etf_element.select(".field_change_1_day")[0].text.strip(),
        'geography_investment_name': etf_element.select(".field_geography_investment_name")[0].text.strip(),
        'investment_object_name': etf_element.select(".field_investment_object_name")[0].text.strip(),
        'sector_name': etf_element.select(".field_sector_name")[0].text.strip(),
    })


if __name__ == "__main__":
    url = get_env_by_name('etf_url')
    scrap_page(url)
