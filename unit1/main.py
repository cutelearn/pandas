import pandas as pd

url = "http://www.taiwanrate.com/"

currency_list = pd.read_html(url)
currency = pd.DataFrame(currency_list[5])
currency = currency[0:].reset_index(drop=True)

print(currency)