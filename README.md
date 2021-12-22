# Description
Program that uses the http://open-notify.org/Open-Notify-API API
to retieve the current location of the ISS space station and 
who is currently in space and what space craft they are on.

## How to use
Program utilizes Typers CLI command functionalty. See [Typer](https://typer.tiangolo.com/)  
In the windows CLI navigate to the folder the main.py program is in  
Then in the CLI type the following to get the space station location.

      input -> python main.py get-current-location
        
      output -> 'The ISS latitude position is : -43.4396'
      output -> 'The ISS longitude position is : -41.7107'
      
There are 2 commands that can be used. 

       Commands:
         1. get-current-location
         2. get-people-craft
         
You can also use Typers built in help fuction from the CLI. 
    
       Input -> python main.py --help
        
       otput -> Usage: main.py [OPTIONS] COMMAND [ARGS]...

        Options:
          --install-completion [bash|zsh|fish|powershell|pwsh]
                                          Install completion for the specified shell.
          --show-completion [bash|zsh|fish|powershell|pwsh]
                                          Show completion for the specified shell, to
                                          copy it or customize the installation.
          --help                          Show this message and exit.

        Commands:
          get-current-location  Prints out the current longitude and latitud...
          get-people-craft      Prints out who is currently in space and the what...
          
# Requirements
Typer  
Requests
