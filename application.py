from flask import Flask
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
import io

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"