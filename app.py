import os
import json
import requests

from os.path import join, dirname
from flask import Flask, request, redirect, url_for
from rauth import OAuth2Service

from dotenv import load_dotenv

app = Flask(__name__)

BASE_URL = "https://api.freshbooks.com"

# Dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# Freshbooks OAuth2
freshbooks = OAuth2Service(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    name="freshbooks",
    authorize_url="https://my.freshbooks.com/service/auth/oauth/authorize",
    access_token_url="https://api.freshbooks.com/auth/oauth/token",
    base_url=BASE_URL,
)


@app.route("/")
def index():
    return "Hello HTN '19!", 200


@app.route("/login")
def login():
    redirect_uri = url_for("authorized", _external=True, _scheme='https')
    params = {"redirect_uri": redirect_uri,
              "response_type": "code"}

    authorize_url = freshbooks.get_authorize_url(**params)
    print(authorize_url)
    return redirect(authorize_url)


@app.route("/authorized")
def authorized():
    redirect_uri = url_for("authorized", _external=True, _scheme='https')
    data = dict(code=request.args["code"], redirect_uri=redirect_uri)
    print(data)
    session = freshbooks.get_auth_session(data=data)
    return session.get("me").json()


@app.route("/test-auth")
def test_auth():
    redirect_uri = url_for("authorized", _external=True, _scheme='https')
    auth_code = request.args.get('code')
    auth_data = { 
        "grant_type": "authorization_code",
        "client_secret": os.getenv('CLIENT_SECRET'),
        "code": auth_code,
        "client_id": os.getenv('CLIENT_ID'),
        "redirect_uri": redirect_uri
    }
    auth_request = requests.post(BASE_URL + "/auth/oauth/token", json=auth_data)
    access_token_dict = json.loads(auth_request.text)
    headers = {"Authorization": "Bearer " + access_token_dict["access_token"]}
    identity_request = requests.get(BASE_URL + "/auth/api/v1/users/me", headers=headers)
    identity_dict = json.loads(identity_request.text)
    profile_dict = identity_dict["response"]["profile"]
    response = "You have successfully logged in for " + profile_dict["first_name"] + " " + profile_dict["last_name"]
    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
