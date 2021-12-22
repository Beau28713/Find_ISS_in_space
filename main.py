import json
import requests
from pprint import pprint

def get_request() -> dict: 
    """Get request from url
    Print's the staus off the connection.
    save data to json file
    return's the request in a json format using the built in json decoder in the request library.
    """
    returned_data = requests.get("http://api.open-notify.org/astros.json")

    print(f"The status code is: {returned_data.status_code}")

    data = returned_data.text # put in string format to be writen to file

    with open("j_data.json", "w") as file:
        json.dump(data, file)

    return returned_data.json()

def print_data(data_obj: dict):
    """Create a formated string of the json data
    dump it to a string"""

    text = json.dumps(data_obj, sort_keys=True, indent=4)
    print(text)

def people_craft(data_obj: dict):
    for people in data_obj["people"]:
        print(f"{people['name']} is on the {people['craft']}")

def main():
    data = get_request()
    # print_data(data)
    people_craft(data)



if __name__ == "__main__":
    main()
