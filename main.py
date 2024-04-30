from bs4 import BeautifulSoup
import requests
import smtplib

def track_amazon_price(url, target_price, sender_email, sender_password):
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36}",
        "sec-ch-ua": 'Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"'
    }

    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, "lxml")

    price_whole = soup.find_all(name="span", class_="a-price-whole")[0].get_text()
    price_fraction = soup.find_all(name="span", class_="a-price-fraction")[0].get_text()
    price = float(price_whole + "." + price_fraction)

    if price <= target_price:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(sender_email, sender_password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=[sender_email],
                msg=f"Subject: Price Alert!\n\n The price is now {price}"
            )

# Example usage:
if __name__ == "__main__":
    url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
    target_price = 99.95
    sender_email = "xyz.123@gmail.com"
    sender_password = "1233()()"
    track_amazon_price(url, target_price, sender_email, sender_password)
