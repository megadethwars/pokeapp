import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, current_app, render_template
from src.appinit import create_app
from flask_cors import CORS
from src.config import app_config
from flask_restx import Api, fields, Resource
from src.views.pocketView import nsPocket

load_dotenv()
env_name = 'local'
port = os.getenv('FLASK_PORT')
env_name = os.getenv('FLASK_ENV')

app = create_app(env_name)
app = Flask(__name__)


cors = CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
    
app.config.from_object(app_config[env_name])


api = Api(app,title="Poke API", version="1.1", description="A simple poke API",)


api.add_namespace(ns=nsPocket,path="/api/v1/pocket")

@app.route("/home")
def home():
  return render_template("index.html")

if __name__ == '__main__':

  # run app
    app.run(debug=True,host='0.0.0.0',port=port)