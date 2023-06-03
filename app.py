import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, current_app, render_template
from src.appinit import create_app

load_dotenv()
env_name = 'local'
port = os.getenv('FLASK_PORT')
env_name = os.getenv('FLASK_ENV')
print(env_name)
app = create_app(env_name)

@app.route("/index")
def index():
  return render_template("index.html")

if __name__ == '__main__':

  # run app
    app.run(debug=True,host='0.0.0.0',port=port)