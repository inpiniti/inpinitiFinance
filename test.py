import ifinance as dt

api_key = ''

dt.set_api_key(api_key)

# df = dt.get_financial_dataframe('005930')
# print(df)

df = dt.get_sector_dataframe()
print(df)

df = dt.get_stock_dataframe('G101010')
print(df)

df = dt.get_monthly_stock_dataframe('KR7005930003')
print(df)