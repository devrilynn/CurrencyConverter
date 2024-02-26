#
# source URL: https://www.geeksforgeeks.org/use-jsonify-instead-of-json-dumps-in-flask/,
#             https://www.fullstackpython.com/flask-json-jsonify-examples.html

from flask import Flask, request, jsonify
from currency import get_exchange_rate, get_valid_currencies

app = Flask(__name__)

@app.route('/convert_currency', methods=['POST'])
def convert_currency():
    """
    Converts currency based on the user input.
    
        from_currency: 3 letter currency code to convert from
        to_currency: 3 letter currency code to convert to
        convert_amount: the amount of money to convert

    Returns:
        JSON response with converted amount or an error message
    """
    # Extracts data from JSON data and convert currency codes to uppercase
    from_currency = request.json.get('from_currency', '').upper()
    to_currency = request.json.get('to_currency', '').upper()
    convert_amount = request.json.get('convert_amount', 0)
    
    # Use for debugging
    print(f"Request received: from {from_currency} to {to_currency} amount {convert_amount}") 

    # Validation
    if not from_currency or not to_currency or convert_amount <= 0:
        print("Validation failed")  
        return jsonify({"Error": "Missing or invalid input"})
    
    # This is where currency conversion occurs
    converted_amount = get_exchange_rate(from_currency, to_currency, convert_amount)
    print(f"Converted amount: {converted_amount}") 

    if converted_amount is not None:
        # Returns successful response with converted amount
        return jsonify({
            "from_currency": from_currency,
            "to_currency": to_currency,
            "original_amount": convert_amount,
            "converted_amount": converted_amount
        })
    else:
        # Error with conversion
        return jsonify({"error": "Currency conversion has failed."})
   

@app.route('/save_currency', methods=['POST'])
def save_currency():
    """
    Saves the users preferred currency to a txt file
    
    JSON data is received with the 3 letter currence code - preferred_currency

    Returns:
        JSON response with success or failure
    """
    # Extracts users preferred currency to save
    preferred_currency = request.json.get('preferred_currency').upper()
    
    # validate preferred currency
    valid_currencies = get_valid_currencies()
    if preferred_currency not in valid_currencies:
        return jsonify({"error": "Invalid currency code"})
    
    # Save preferred currency to txt file
    preferences_string = f"{preferred_currency}\n"
    file_path = 'user_preferences.txt'
    
    # Write & handle errors
    try:
        with open(file_path, 'a') as file:
            file.write(preferences_string)
    except IOError as e:
        print(f"An error occurred while attempting to write this file: {e}")
        return jsonify({"error": "Could not save the currency preference"})

    return jsonify({"message": "Currency preference has saved successully."})
 
 
if __name__ == '__main__':
    app.run(debug=True)
