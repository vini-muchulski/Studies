from datetime import datetime, timedelta
#data 
hoje = datetime.now()
print(hoje.date())

amanha = hoje + timedelta(days=7)
print(amanha)

data_entrada_UFSC = datetime(year=2022,month=8,day=25)

tempo_na_UFSC = hoje - data_entrada_UFSC

print(tempo_na_UFSC.days)

#formato br
hoje_formatado = hoje.strftime("%d/%m/%Y")
print(hoje_formatado)

#calculo de fuso horario
hoje = hoje - timedelta(hours=2)
print(hoje)

