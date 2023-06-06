import requests
import time
from datetime import datetime

def get_usd_ars_exchange_rate():
    url = 'https://mercados.ambito.com/dolar/informal/variacion'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        compra = data['compra']
        venta = data['venta']
        return compra, venta
    else:
        return None, None

# Set end time to 3 PM
end_time = datetime.now().replace(hour=22, minute=0, second=0, microsecond=0)  

while datetime.now() < end_time:
    compra_rate, venta_rate = get_usd_ars_exchange_rate()

    if compra_rate is not None and venta_rate is not None:
        print(f"USD/ARS Exchange Rate - Compra: {compra_rate}, Venta: {venta_rate}")
    else:
        print("Failed to fetch USD/ARS exchange rate.")

    # Delay for 2 minutes (120 seconds)
    time.sleep(60)
