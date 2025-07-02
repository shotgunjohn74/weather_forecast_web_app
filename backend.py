import requests as req

api_key = "213895fe5f29cce58dfa7abc2e1801d7"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}&units=imperial&lang=en"

    info = req.get(url).json()

    filtered_data = info["list"]

    filter_days = 8 * days

    filtered_data = filtered_data[:filter_days]

    return filtered_data

if __name__ == "__main__":
    get_data("Gillette", 3)