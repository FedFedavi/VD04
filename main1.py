import flask
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def time():
    date = datetime.now()
    form_date = date.strftime("%d-%m-%Y %H:%M:%S")
    return f"Текущая дата и время: {form_date}"

@app.route("/time/")
def time_html():
    date = datetime.now()
    form_date = date.strftime("%d-%m-%Y %H:%M:%S")
    html = f"""
        <html>
        <head>
            <title>Текущее время</title>
        </head>
        <body>
            <h1>Текущая дата и время:</h1>
            <p>{form_date}</p>
        </body>
        </html>
        """
    return html

if __name__ == "__main__":
    app.run()