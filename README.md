# inteliPaste
inteliPaste uses a simple infinite loop to scan the clipboard for URLs and when it finds one, it request the Google URL shortener API to create a new shortened URL and writes it in the clipboard.

## Dependencies
To have access to the clipboard, it uses the [pyperclip](https://github.com/asweigart/pyperclip) so it should be installed:
`pip install pyperclip`.

To create the HTTP requests to the google API: `pip install requests`.

To download the library and set up a project on google developer console follow [here](https://developers.google.com/api-client-library/python/apis/urlshortener/v1).

## Installation
The first thing you should do (after installing all dependencies) is set up a project on the developers console and add API key credentials. Then create a environment variable with the key by the name of API_KEY*.
* If you are on linux, run the following command on terminal: `export API_KEY="key=YoUrAp1K3yHere"`.
* As an alternative for the environment variable, you can uncomment line 10 (and comment line 9) and use the `API_KEY` as a local variable (beware of the risks of keep such information on code). 

*IMPORTANT OBSERVATION: in order to persist the environment variable, you should add to you system. 

Now you are ready to go, just run `python intellipaste.py` and start receiving shortened URLs on the clipboard. as an alternative to execute the scrip every time, you can add it as a cron job (linux only).
* First, give execution permission: `chmod +x intellipaste.py`
* Now, on terminal run `crontab -e` and add `@reboot /path/to/script/intellipaste.py`.

If you are on windows, you can compile the application as a standalone (not really standalone) binary with [PyInstaller](http://www.pyinstaller.org/), its super easy, install and you are ready to go and add it to start with the system. Or you can set up a .bat file that executes `python intellipaste.py` and add it as well.
