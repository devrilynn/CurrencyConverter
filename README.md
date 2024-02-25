# CurrencyConverter

This microservices converts currencies by utilizing the Frankfurter API to get real-time exchange rate data.

### Requesting Data from the Microservice

To requst data from this microservice you should make a POST request to /convert_currency endpoint with a JSON payload contatining these fields:
from_currency: This is the three letter currency code the user will be converting from
to_currency: Tis is the three letter currency code the user is converting to
convert_amount: This is the amount of money that needs to be converted


### Receiving Data from the Microservice

This microservice will respond with a JSON payload that has this information:
from_currency: The three letter currency code of the original amount.
to_currency: The three letter currency code of the converted amount.
original_amount: The original amount of money before conversion.
converted_amount: The converted amount of money in the chosen currency.
