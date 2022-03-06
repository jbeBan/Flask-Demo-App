# Flask Demo App

A simple Flask application to demonstrate its use.

---

**NOTE: None of the information presented and/or contained within this project is meant to represent real and/or established companies/organizations and has all been generated as mock data. If for some reason the data contained within `market_orders.json` represents your information, feel free to contact me and I will remove it.**

---

## How to Download and Run the App

You must have Python installed and set as a PATH variable for the following instructions to work. If you get an error stating `Python was not found;` when running the first command, try replacing `python` with `python3`.

> ### Download
> ---
> To download the app, click on the `Code` button and select the `Download ZIP` option. Make sure to save the zip file somewhere that is easy to reach with the command line/bash. After saving the zip file to your desired location, extract the zip file.

> ### Run
> ---
> To run the app, open the folder within the extracted folder with git bash (the following commands have only been tested in git bash and will not work in command line/powershell, but they might work in linux) and run the following commands:
>
> `python -m venv venv # Creates a virtual environment`
>
> `. venv/scripts/activate # Activates the virtual environment`
>
> `pip install -r requirements.txt # Installs the necessary packages in the virtual environment`
>
> `flask run # Runs the app`
>
> After the app is up and running (you should get a message displayed in the console that ends with ` * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`), hold the `Ctrl` or `command` key down and click on the link. You can also type in the url in a browser yourself, if you prefer to do it that way.

> ### Stop
> ---
> To stop the app, press `CTRL+C` in git bash. After stopping the app, run the command `deactivate` in git bash to deactivate the virtual environment.

> ### Rerun
> ---
> To run the app again, you only have to run the following commands in git bash:
>
> `. venv/scripts/activate # Activates the virtual environment`
>
> `flask run # Runs the app`
