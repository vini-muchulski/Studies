import holidays


# pypi.org/project/holidays/

feriados =  holidays.country_holidays("BR", subdiv="RS")
feriados_2024 = feriados["2024-01-01":"2024-12-31"]

print(feriados["2024-09-20"])