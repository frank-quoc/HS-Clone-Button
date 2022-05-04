# HS-Clone-Button
HubSpot is an American developer and marketer of software products for inbound marketing, sales, and customer service. It frustratingly does not have a clone button for deals.

## Table of Contents

1. [About The Project](README.md#about-the-project)
2. [Getting Started](README.md#getting-started)
    * [Installation](README.md#installation)
    * [Setting Up](README.md#setting-up)
3. [Contact](README.md#contact)
4. [Acknowledgements](README.md#acknowledgements)

## About the Project

A way to clone a Hubspot deal, using a "checkbox" property which adds a year to the close date, and that new close date to the deal name to differentiate from the original deal. The boolean value of true in the checkbox, will trigger a webhook to activate the program to use a GET request to obtain the original data and then a POST request to clone the deal with the formatted close date and deal name. 

## Getting Started

In order to run the application, install and do the following in an Ubuntu Linux Environment

### Installation

Clone the repo

```git clone https://github.com/frank-quoc/HS-Clone-Button```

Install required libraries from ```requirements.txt```
  * click==8.0.3
  * python-dateutil==2.8.2
  * Flask==2.0.2
  * gunicorn==20.1.0
  * itsdangerous==2.0.1
  * Jinja2==3.0.3
  * MarkupSafe==2.0.1
  * requests==2.22.0
  * Werkzeug==2.0.2

```pip3 install -r requirements.txt```

### Setting Up
1. Hubspot workflow should get a trigger for when the clone "checkbox" property changes it activates the webhook.
2. Use **flask** and **ngrok.com** to set up a server for local testing. Flask to set up the server and ngrok.com to open a specific port to accept data from and give a url to put in the Hubspot workflow.
    1. Create a virtual environment (in command line): ```python3 -m venv /path/to/new/virtual/environment```
    2. Activate virtual environment (in command line): ```source /path/to/venv/bin/activate```
    3. After setting up an account, follow directions to use ngrok: https://dashboard.ngrok.com/get-started/setup
3. Step 2 can be deactivated, once a live server is needed, use Heroku.
    1. After creating an account and making the app, follow these steps: https://dashboard.heroku.com/apps/hs-clone-deals/deploy/heroku-git
    2. Obtain Heroku endpoint to place in workflow.

## Contacts

Frank Ho - [@cuLyTech](https://twitter.com/culyTech)

Project Link: [https://github.com/frank-quoc/HS-Clone-Button.git](https://github.com/frank-quoc/HS-Clone-Button.git)

## Acknowledgements
[Obo Agency](https://theobogroup.com/careers/) 

