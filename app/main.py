from flask import Flask, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("postgresql://qttgloeftjasgq:6ee694584f865888de3969ea9c6196a74435377c44b382d0ab4a8a3f529fe0c4@ec2-34-234-12-149.compute-1.amazonaws.com:5432/dfofff6l7k23vb")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


app = Flask(__name__,template_folder="static/templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
