import requests as req

api_key = "213895fe5f29cce58dfa7abc2e1801d7"


def get_data(place, days, option_type):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"

    info = req.get(url).json()

    filtered_data = info["list"]

    filter_days = 8 * days

    filtered_data = filtered_data[:filter_days]

    if option_type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    elif option_type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data

if __name__ == "__main__":
    get_data("Gillette", 3, "temperature")