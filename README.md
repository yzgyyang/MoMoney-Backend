# MoMoney-Backend

## Running the Flask app

- Make sure you have [Python3](https://www.python.org/downloads/) installed on your computer.
- Clone this repo into your computer.
- Create a new **.env** file in the root folder of the project. The .env file should at least contain the following variables
```
CLIENT_ID='<YOUR-CLIENT-ID>'
CLIENT_SECRET='<YOUR-CLIENT-SECRET>'
REDIRECT_URL='<YOUR-REDIRECT-URI>'
```
The values for these variables are available on the [developer page](https://my.freshbooks.com/#/developer)
- Install all the dependencies by running the following commands
```
$ pipenv install
$ pipenv shell
```
- Run the app using the Flask command.
```
$ flask run --cert=adhoc
```
- Click on the **Authorizaton URL** for you application available on the [developer page](https://my.freshbooks.com/#/developer)
- Login to the FreshBooks application using the credentials for the test account given to you during the hackathon.
If you have correctly set up you application on **FreshBooks** and entered your credentials on the **.env** file you should get the following output.
```
You have successfully logged in for First Last
```

If you can see the above output, congrats you can now start building!
