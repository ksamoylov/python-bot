def to_html(etfs: list) -> list:
    html = "<table>"
    
    for etf in etfs:
        html += "<tr>"
        html += f"<td>{etf.get_fund_comp_name()}</td>"
        html += f"<td>{etf.get_change_one_day()}</td>"
        html += f"<td>{etf.get_currency_name()}</td>"
        html += f"<td>{etf.get_sector_name()}</td>"
        html += f"<td>{etf.get_investment_object_name()}</td>"
        html += "</tr>"
        
    html += "</table>"
    css = "table, th, td {border: 1px solid black;} table {background-color: white}"

    return html, css

