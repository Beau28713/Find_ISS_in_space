"""
Uses the http://open-notify.org/Open-Notify-API
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
        returned_data = requests.get("http://api.openotify.org/astros.json")

        typer.echo(f"The status code is: {returned_data.status_code}\n")

        data_dict = returned_data.json()

        for people in data_dict["people"]:
            typer.echo(f"{people['name']} is on the {people['craft']}")
    
    except BaseException as error:
        typer.echo("The error was:")
        typer.echo(f"{error}")

    

@iss.command()
def get_current_location():
    """Prints out the current longitude and latitud location of the ISS space station"""
    try:
        returned_data = requests.get("http://api.open-notify.org/iss-now.json")

        typer.echo(f"The status code is: {returned_data.status_code}\n")

        data_dict = returned_data.json()

        map_data = requests.get(f"https://api.wheretheiss.at/v1/coordinates/{data_dict['iss_position']['latitude']},{data_dict['iss_position']['longitude']}")

        map_dict = map_data.json()

        typer.echo(f"The ISS latitude position is : {data_dict['iss_position']['latitude']}")
        typer.echo(f"The ISS longitude position is : {data_dict['iss_position']['longitude']}")
        typer.echo(f"current map location is {map_dict['timezone_id']}")
        typer.echo(f"Country code is {map_dict['country_code']}")
        typer.echo("***Note negative numbers represent South latitude and West Longitude and positive represents North and East***")

    except BaseException as error:
        typer.echo("The error was:")
        typer.echo(f"{error}")

if __name__ == "__main__":
    iss()
