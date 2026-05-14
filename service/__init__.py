"""
Package initialization for the Accounts Service
"""
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

talisman = Talisman(app, force_https=False)
CORS(app)

from service import routes, config  # noqa: E402, F401
