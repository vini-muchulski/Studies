import pandas_market_calendars as mcal

#pypi.org/project/pandas-market-calendars/

# BOLSA DE VALORES DE SAO PAULO
calendario = mcal.get_calendar("BMF")
#print(calendario)

dias_negociacao = calendario.schedule(start_date="2024-01-01", end_date="2024-12-31")
print(dias_negociacao)

