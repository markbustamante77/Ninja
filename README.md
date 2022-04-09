# Ninja example

#### Required Software for local runs
* [homebrew](https://brew.sh/)
* [Google Chrome](https://www.google.com/chrome/)
* [chromedriver](https://chromedriver.chromium.org/downloads)

These commands assume you already have homebrew and Chrome/Firefox installed  
Run these commands to setup a local environment:
* Install Python3 if not already installed 
    * `brew install python3`
* Install chromedriver (necessary for Selenium to control Chrome)
    * `brew cask install chromedriver`
* Install virtualenv if not already installed
    * `pip3 install virtualenv`
* Create a virtual python environment
    * `virtualenv venv -p python3`
* Activate the local environment (This will have to be done on every new shell)
    * `source venv/bin/activate`
* Install the python requirements
    * `pip install -r requirements.txt`

## Running Tests Locally
Tests can be run using the local chromedriver. Local chromedriver must be set in PATH

Please refer to Ninja project README.md files for how to start up server and launch UI.

Environment command `--api 'API_URL'` set for api url
Environment command `--api 'UI_URL'` set for ui url