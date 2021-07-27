class Etf:
    fund_comp_name: str
    latest_quotation_date: str
    currency_name: str
    close: str
    change_one_day: str
    geography_investment_name: str
    investment_object_name: str
    sector_name: str
    
    def __init__(
            self,
            fund_comp_name: str,
            latest_quotation_date: str,
            currency_name: str,
            close: str,
            change_one_day: str,
            geography_investment_name: str,
            investment_object_name: str,
            sector_name: str
    ):
        self.fund_comp_name = fund_comp_name
        self.latest_quotation_date = latest_quotation_date
        self.currency_name = currency_name
        self.close = close
        self.change_one_day = change_one_day
        self.geography_investment_name = geography_investment_name
        self.investment_object_name = investment_object_name
        self.sector_name = sector_name
    
    def get_fund_comp_name(self) -> str:
        return self.fund_comp_name
    
    def get_latest_quotation_date(self) -> str:
        return self.latest_quotation_date
    
    def get_currency_name(self) -> str:
        return self.currency_name
    
    def get_close(self) -> str:
        return self.close
    
    def get_change_one_day(self) -> str:
        return self.change_one_day
    
    def get_geography_investment_name(self) -> str:
        return self.geography_investment_name
    
    def get_investment_object_name(self) -> str:
        return self.investment_object_name
    
    def get_sector_name(self) -> str:
        return self.sector_name
