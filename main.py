from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    context = {
        'poem': ['На рассвете солнце всходит',
                'Светит ярко, мир живит',
                'Ветер легкий, поле водит',
                'Травы шепчут, лес молчит',
                'Птицы песнь свою заводят',
                'В небе синим тает след',
                'Новый день к себе приводит',
                'Жизни дарит вновь привет']
    }
    return render_template("shablon.html", **context)

@app.route("/shablon/")
def index2():
    context = {
        'caption': 'Шаблон индекса',
        'link': 'Улыбнитесь Каскадеры'
    }
    return render_template("index.html", **context)

@app.route("/blog/")
def blog():
    return render_template("blog.html")

@app.route("/contacts/")
def cont():
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run()

