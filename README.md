# CurrencyConverter

This microservices converts currencies by utilizing the Frankfurter API to get real-time exchange rate data.

### Requesting Data from the Microservice

To requst data from this microservice you should make a POST request to /convert_currency endpoint with JSON data contatining these fields:

from_currency: This is the three letter currency code the user will be converting from
to_currency: Tis is the three letter currency code the user is converting to
convert_amount: This is the amount of money that needs to be converted

## Example Call

 {
    "from_currency": "USD",
    "to_currency": "GBP",
    "convert_amount": 120.00
  }

### Receiving Data from the Microservice

This microservice will respond with JSON data that has this information:

from_currency: The three letter currency code of the original amount.
to_currency: The three letter currency code of the converted amount.
original_amount: The original amount of money before conversion.
converted_amount: The converted amount of money in the chosen currency.

## Example Response

 {
    "from_currency": "USD",
    "to_currency": "GBP",
    "convert_amount": 120.00,
    "converted_amount": 94.53
  }

 UML Diagram:
 
[UML - Currency Converter.pdf](https://github.com/devrilynn/CurrencyConverter/files/14410813/UML.-.Currency.Converter.pdf)
