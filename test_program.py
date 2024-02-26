# 
# Code incorporated from source URL: https://www.youtube.com/watch?v=snPGUT-Fxa4,
#                                    https://www.frankfurter.app/docs/

import requests
from currency import get_valid_currencies

# API used to convert currency
FRANKFURTER_API_URL = "https://www.frankfurter.app/"
    
def save_currency_preference(to_currency):
    """
        : This function saves the users preferred currency to a txt file
    """
    # URL of your microservice for saving currency preference
    url = 'http://localhost:5000/save_currency'

    # data with the preferred currency
    data = {
        'preferred_currency': to_currency
    }
    
    
    # Make the POST request to save the preferred currency
    response = requests.post(url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Currency preference saved successfully.")
    else:
        print(f"Failed to save currency preference. Status code: {response.status_code}, Message: {response.text}")


def test_currency_conversion():
    """
        : This function tests the currency conversion.
        : Receives input from the user on the currency to convert from, what currency to convert to, and the amount to convert.
        :  
        : This uses the get_valid_currencies method to fetch valid currency codes to ensure valid currencies before performing conversion.
        : Once input is valid, a POST request is made to currency conversion microservice providing: from_currency, to_currency, convert_amount.
    """
    valid_currencies = get_valid_currencies()

    # Validate currency code entered
    while True:
        from_currency = input("Enter the currency you want to convert from (e.g. USD): ").upper()
        if from_currency in valid_currencies:
            break
        print("Invalid currency code. Please enter a valid currency code.")

    # Validate currency code entered
    while True:
        to_currency = input("Enter the currency you want to convert to (e.g. GBP): ").upper()
        if to_currency in valid_currencies:
            break
        print("Invalid currency code. Please enter a valid currency code.")

    # Validate numerical value
    while True:
        try:
            convert_amount = float(input("Enter the amount you want to convert: $"))
            break
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")

    # Insert the URL of your microservice
    url = 'http://localhost:5000/convert_currency'

    # data to convert
    data = {
        'from_currency': from_currency,
        'to_currency': to_currency,
        'convert_amount': convert_amount
    }

    # Make the POST request
    response = requests.post(url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response data
        data = response.json()
        print(f"Converted Amount: ${data['original_amount']:.2f} {data['from_currency']} is equivalent to ${data['converted_amount']:.2f} {data['to_currency']}")
        
        # Ask the user if they want to save this currency preference
        save_preference = input(f"Do you want to save {to_currency} as your preferred currency? (yes/no): ").lower()
        if save_preference == 'yes':
            save_currency_preference(to_currency)
    else:
        # Print error message
        print(f"Failed to convert currency. Status code: {response.status_code}, Message: {response.text}")

if __name__ == "__main__":
    test_currency_conversion()
