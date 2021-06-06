import os
from flask import Flask

app = Flask(__name__)

# additional code

color = "red"
# color = os.environ.get('APP_COLOR')

"""
to run with terminal
$ export APP_COLOR=blue; python web_app

to run with docker
$ docker run -e APP_COLOR=blue web_app.py
"""

@app.route("/")
def main():
  print(color)
  return render_template("index.html", color=color)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8080")
