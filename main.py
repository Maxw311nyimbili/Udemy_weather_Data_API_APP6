from flask import Flask, render_template

# web framework manages multiple web pages. It is responsible to ensure that the
# web pages interact with each other as intended

# to use the flask framework you need to import the class Flask and render_template
# ensure to put your html files in a directory called "templates" as flask is meant to
# look for html files in a templates' folder.

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station, "date": date, "temperature": temperature}


# ensures that error encountered are displayed on the browser
# __name__: this is equal to "__main__" if you print __name__ and run the script, the value will be "__main__"
# but if you import the file that contains __name__, then run that file, __name__ will adopt the name of that file
# Hence, the condition if __name__ == "__main__": means that execute the lines of code under this conditional if the
# script is executed directly, and not when it is imported in another file.
if __name__ == "__main__":
    app.run(debug=True)
