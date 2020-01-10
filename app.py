from flask import Flask, render_template
from flask import request
import data

app = Flask(__name__)


@app.route('/')
def hello():
    output = render_template("index.html",
                             title=data.title,
                             departures=data.departures,
                             subtitle=data.subtitle,
                             description=data.description,
                             tours=data.tours)
    return output


@app.route('/from/<direction>')
def directions(direction):

    tours_from_direction = []
    for t in data.tours.values():
        if t['departure'] == direction:
            tours_from_direction.append(t)

    output = render_template("direction.html",
                             title=data.title,
                             departures=data.departures,
                             direction=direction,
                             tours=data.tours,    # все туры
                             tours_from_direction=tours_from_direction)   # только туры по направлению
    return output


@app.route('/tours/<id>')
def tours(id):
    output = render_template("tour.html",
                             title=data.title,
                             departures=data.departures,
                             tour=data.tours[int(id)])
    return output


# роут с дополнительными параметрами, типа ?key=value
@app.route('/search/')
def search():
    return "Выполняем поиск по строке " + request.values.get("s")


@app.errorhandler(404)
def not_found(e):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def server_error(e):
    return "Что-то не так, но мы все починим"


if __name__ == '__main__':
    app.run()
