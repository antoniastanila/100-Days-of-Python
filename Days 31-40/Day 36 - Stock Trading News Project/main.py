import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "your_API_key"
NEWS_API_KEY = "your_API_key"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(
    url="https://www.alphavantage.co/query", params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) -
                 float(day_before_yesterday_closing_price))
diff_price = (difference/float(yesterday_closing_price)) * 100
print(diff_price)

if diff_price > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title",
    }
    news_response = requests.get(
        url="https://newsapi.org/v2/everything", params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    three_articles = articles[:3]
    for index in range(len(three_articles)):
        with open(f"art_{index}.txt", "w") as data_file:
            data_file.write(
                f"Title: {three_articles[index]['title']}\nBrief: {three_articles[index]['description']}")


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME and write them in separate files.
