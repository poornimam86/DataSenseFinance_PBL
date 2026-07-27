import requests


class APIService:

    def get_exchange_rates(self):

        url = "https://open.er-api.com/v6/latest/INR"

        try:
            response = requests.get(url, timeout=5)

            response.raise_for_status()

            data = response.json()

            print("===================================")
            print("   LIVE EXCHANGE RATES")
            print("===================================")

            print("Base Currency :", data["base_code"])
            print("USD :", data["rates"]["USD"])
            print("EUR :", data["rates"]["EUR"])
            print("GBP :", data["rates"]["GBP"])

        except requests.exceptions.RequestException:
            print("Unable to fetch exchange rates.")
            print("Please check your internet connection and try again.")