Amazon Price Tracker

This Python script allows users to track prices of products on Amazon and receive email notifications when the price drops below a specified target price.

Features

Fetches the current price of a product on Amazon using BeautifulSoup and requests.
Sends email notifications using Gmail SMTP when the price drops below the specified target price.
Easy-to-use interface with customizable target price, Amazon product URL, sender email, and sender email password.


Installation

Clone this repository to your local machine:


git clone https://github.com/MohamedHelmyCG/amazon-price-tracker.git

Install the required dependencies:


pip install beautifulsoup4 requests


Usage
Modify the url, target_price, sender_email, and sender_password variables in the if __name__ == "__main__": block of the script (amazon_price_tracker.py) with your desired values.

Run the script:

python amazon_price_tracker.py

The script will check the price of the product at the specified URL on Amazon. If the price drops below or equal to the target price, you will receive an email notification at the specified sender email address.
Contributing.

Contributions are welcome! Please feel free to submit any issues or pull requests.



