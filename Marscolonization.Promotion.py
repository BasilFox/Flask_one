from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса!"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    sp = ['Человечество вырастает из детства.',

          'Человечеству мала одна планета.',

          'Мы сделаем обитаемыми безжизненные пока планеты.',

          'И начнем с Марса!',

          'Присоединяйся!']
    return '</br>'.join(sp)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Mars colonization</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!<h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <h3>Вот она какая, красная планета.<h3>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    sp = ['Человечество вырастает из детства.',

          'Человечеству мала одна планета.',

          'Мы сделаем обитаемыми безжизненные пока планеты.',

          'И начнем с Марса!',

          'Присоединяйся!']
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                     {sp[0]}
                    </div>
                    <div class="alert alert-secondary" role="alert">
                     {sp[1]}
                    </div>
                    <div class="alert alert-success" role="alert">
                     {sp[2]}
                    </div>
                    <div class="alert alert-danger" role="alert">
                     {sp[3]}
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
