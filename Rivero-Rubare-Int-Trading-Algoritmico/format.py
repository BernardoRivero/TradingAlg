import pandas as pd

simbolo = "MSFT"

# Lee el archivo 
data = pd.read_csv("MSFT Historical Data.csv")

# Convierte la columna 'Date' al formato deseado
data['Date'] = pd.to_datetime(data['Date'], format="%m/%d/%Y").dt.strftime("%Y-%m-%d")

# Renombra la columna 'Price' a 'Close'
data = data.rename(columns={"Price": "Close"})

data['Adj Close'] = data['Close']

# Reorganiza las columnas en el orden deseado
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close"]]

data = data.sort_values(by="Date")

# Guarda el CSV con las fechas formateadas
data.to_csv(simbolo+".csv", index=False)
