import requests
import json

SHIP_URL = "https://swapi.dev/api/starships/10"


def get_ship(url):
    response = requests.get(url)
    data = response.json()
    ship_info = {
        'name': data['name'],
        'max_speed': data['max_atmosphering_speed'],
        'class': data['starship_class'],
        'pilots': []
    }

    for pilot_url in data['pilots']:
        pilot_response = requests.get(pilot_url)
        pilot_data = pilot_response.json()
        pilot_info = {
            'name': pilot_data['name'],
            'height': pilot_data['height'],
            'weight': pilot_data['mass'],
            'home_planet': requests.get(pilot_data['homeworld']).json()['name'],
            'planet_link': pilot_data['homeworld']
        }
        ship_info['pilots'].append(pilot_info)

    return ship_info


def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    ship_data = get_ship(SHIP_URL)
    save_to_json(ship_data, "millennium_falcon.json")
