from flask import Flask
import pickle
import os
from config import basedir

app = Flask(__name__)
app.config.from_object('config')

# print basedir
filename = os.path.join(basedir, "files/objLabelLookup.p")
loader = pickle.load(open(filename, "rb"))

from app import views