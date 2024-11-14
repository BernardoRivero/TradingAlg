import yfinance as yf

# Define el símbolo y el rango de fechas deseado
simbolo = "ORCL"
data = yf.download(simbolo, start="1999-11-11", end="2010-11-11")

# Filtra solo las columnas deseadas y elimina la hora de la fecha
data = data[['Open', 'High', 'Low', 'Close','Volume']]
data.index = data.index.date  # Cambia el índice de datetime a solo fecha

# Guarda el archivo en CSV
data.to_csv(simbolo +".csv", date_format="%Y-%m-%d")
