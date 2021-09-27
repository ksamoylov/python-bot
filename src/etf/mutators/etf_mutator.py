def to_html(etfs: list, page: int) -> list:
    html = f"<header>ETF фонды. Страница: {page}</header>"
    html += "<table>"
    html += "<tr>"
    html += "<th>Название фонда</th>"
    html += "<th>Изменение за день</th>"
    html += "<th>Валюта</th>"
    html += "<th>Сектор</th>"
    html += "<th>Объект</th>"
    html += "<th>Изменение за день</th>"
    html += "</tr>"
    
    for etf in etfs:
        html += "<tr>"
        html += f"<td>{etf.get_fund_comp_name()}</td>"
        html += f"<td>{etf.get_change_one_day()}</td>"
        html += f"<td>{etf.get_currency_name()}</td>"
        html += f"<td>{etf.get_sector_name()}</td>"
        html += f"<td>{etf.get_investment_object_name()}</td>"
        html += f"<td>{etf.get_close()}</td>"
        html += "</tr>"
        
    html += "</table>"
    css = "body {padding: 0; margin: 0; background-color: #f6f8fa} " \
          "table, th, td {border: 1px solid black; margin: 3em auto;} " \
          "header {margin: 1em auto; text-align: center;}"

    return html, css

