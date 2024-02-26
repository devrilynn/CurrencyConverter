import requests

# API used to convert currency
FRANKFURTER_API_URL = "https://www.frankfurter.app/"


def get_valid_currencies():
    """
        : Fetches a list of valid currency codes from the Frankfurter API for validating user input.
    """
    try:
        # API request for valid currency codes
        response = requests.get(f"{FRANKFURTER_API_URL}currencies")

        if response.status_code == 200:
            return response.json()              # Return the list of currencies
        else:
            print("Failed to retrieve valid currencies.")
            return {}                           # Return an empty dictionary if the request fails
        
    except requests.exceptions.RequestException as e:
        print("An error occurred: ", e)


def get_exchange_rate (from_currency, to_currency, convert_amount):
    """
        : This method retrieves and prints the exchange rate from one currency to another for the user's specified amount
        :  
        : Sends a GET request to the Frankfurter API to convert the specified amount
        :   
        : params: 
        :   from_currency: 3 letter currency code to convert from
        :   to_currency: 3 letter currency code to convert to
        :   convert_amount: the amount of money to convert
        :
        : return: The converted amount of money in the specified currency. Returns None if API call fails.
    """
    # Establish API request with frankfurter parameters
    response = requests.get(
        f"{FRANKFURTER_API_URL}/latest?amount={convert_amount}&from={from_currency}&to={to_currency}"
    )

    # Check if API request is successful
    if response.status_code == 200:
        converted_amount = response.json()['rates'][to_currency]
        print(f"${convert_amount:.2f} {from_currency} is ${converted_amount:.2f} {to_currency}")
        return converted_amount
    
    else:
        print(f"Failed to retrieve exchange rates. Status code: {response.status_code}")
        return None
 
    

