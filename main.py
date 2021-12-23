"""
Uses API's http://open-notify.org/Open-Notify-API and https://wheretheiss.at/w/developer
To retieve the current location of the ISS space station and 
who is currently in space and what space craft they are on.

Uses the CLI libray Typer for easier command line interfaces by using
Commannds.

    Commands:
     1. get-current-location
     2. get-people-craft

     Ex.
      input -> python main.py get-current-location
        
      output -> 'The ISS latitude position is : -43.4396'
      output -> 'The ISS longitude position is : -41.7107'
"""
import typer
import requests

iss = typer.Typer()

@iss.command()
def get_people_craft(): 
    """Prints out who is currently in space and the what space craft they are on """
    try:
        people_data = requests.get("http://api.open-notify.org/astros.json", timeout=5)
        people_data.raise_for_status()

        typer.echo(f"The status code is: {people_data.status_code}\n")

        people_dict = people_data.json()

        for people in people_dict["people"]:
            typer.echo(f"{people['name']} is on the {people['craft']}")
    
    except requests.exceptions.HTTPError as httperr:
        typer.echo(httperr)
    except requests.exceptions.Timeout as timerr:
        typer.echo(timerr)
    except requests.exceptions.ConnectionError as conerr:
        typer.echo(conerr)
    except requests.exceptions.RequestException as err:
        print(err)


@iss.command()
def get_current_location():
    """Prints out the current longitude and latitude 
    location of the ISS space station along with its map
    and country code location"""
    try:
        location_data = requests.get("http://api.open-notify.org/iss-now.json")
        location_data.raise_for_status()

        typer.echo(f"The status code is: {location_data.status_code}\n")

        location_dict = location_data.json()

        map_data = requests.get(f"https://api.wheretheiss.at/v1/coordinates/{location_dict['iss_position']['latitude']},{location_dict['iss_position']['longitude']}")

        map_dict = map_data.json()

        typer.echo(f"The ISS latitude position is : {location_dict['iss_position']['latitude']}")
        typer.echo(f"The ISS longitude position is : {location_dict['iss_position']['longitude']}")
        typer.echo(f"current map location is {map_dict['timezone_id']}")
        typer.echo(f"Country code is {map_dict['country_code']}")
        typer.echo("***Note negative numbers represent South latitude and West Longitude and positive represents North and East***")

    except requests.exceptions.HTTPError as httperr:
        typer.echo(httperr)
    except requests.exceptions.Timeout as timerr:
        typer.echo(timerr)
    except requests.exceptions.ConnectionError as conerr:
        typer.echo(conerr)
    except requests.exceptions.RequestException as err:
        print(err)

if __name__ == "__main__":
    iss()
