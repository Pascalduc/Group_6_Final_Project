from flask import Flask, render_template, redirect

# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():


    # Return template and data
    return render_template("Boston Top200 Airbnb Mapping/index.html")

if __name__ == "__main__":
    app.run(debug=True)