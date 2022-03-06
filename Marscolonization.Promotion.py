from flask import Flask, url_for
from flask import request

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


@app.route('/vibor', methods=['POST', 'GET'])
def vibor():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, height = 1000px, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style1.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                              <div style="text-align: center;">
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                                </div>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text " class="form-control" id="surname" placeholder="Введите фамилию." name="surname">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя." name="name">
                                        <div class="form-group">
                                            <label for="classSelect"> </label>
                                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                            <label for="educationSel"> Какое у Вас образование?</label>
                                            <select class="form-control" id="educationSel" name="edu">
                                              <option>Начальное</option>
                                              <option>Основное общее</option>
                                              <option>Среднее общее</option>
                                              <option>Среднее спициальное</option>
                                              <option>Высшие</option>
                                            </select>
                                         </div>
                                        <label for="classSelect">Какие у Вас профессии?</label>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="eng1">
                                            <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                            
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="eng2">
                                            <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="pilot">
                                            <label class="form-check-label" for="acceptRules">Пилот</label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="meteo">
                                            <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="eng3">
                                            <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                        </div>
                                        <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="eng4">
                                            <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                        </div>
                                        <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="exo">
                                            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                        </div>
                                         <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        
                                        
                                        
                                        
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                       
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['edu'])
        print(request.form['eng1'])
        print(request.form['eng2'])
        print(request.form['pilot'])
        print(request.form['meteo'])
        print(request.form['eng3'])
        print(request.form['eng4'])
        print(request.form['exo'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        return "Форма отправлена"


@app.route('/choice/<planet>')
def choice_mars(planet):
    if planet == 'mars':
        sp = ['На ней много необходимых ресурсов;',

              'На ней есть вода и атмосфера;',

              'На ней есть небольшое магнитное поле;',

              'Наконец, она просто красива!',

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
                        <h1>Моё предложение: Марс</h1>
                        <h2>Эта плпнета близка к Земле;</h2>
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
    elif planet == 'mercury':
        sp = ['Там очень тепло;',

              'Удобно исследовать солнце;',

              'Похож на Луну;',

              'Наконец, он просто красив!',
              ]
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
                                <h1>Моё предложение: Меркурий</h1>
                                <h2>Достаточно невелика для быстрого освоения;</h2>
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
    elif planet == 'venus':
        sp = ['Там есть твердая поверхность;',

              'Сущесвует озоновый слой;',

              'Постоянные освежающие ветра;',

              'Наконец, она просто красива!',
              ]
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
                                    <h1>Моё предложение: Венера</h1>
                                    <h2>По ряду характеристик — например, по массе и размерам — Венера считается «сестрой» Земли;</h2>
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
    elif planet == 'jupiter':
        sp = ['Много полезных газов;',

              'Прекрасные полярные сияния',

              'Через пару миллиардов лет появится вода;',

              'Наконец, он просто красив!',
              ]
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
                                    <h1>Моё предложение: Юпитер</h1>
                                    <h2>Юпи́тер — крупнейшая планета Солнечной системы, пятая по удалённости от Солнца;</h2>
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
    elif planet == 'saturn':
        sp = ['Обратим внимание на его спутник Титан;',

              'Титан является единственным, кроме Земли, телом в Солнечной системе, для которого доказано стабильное существование жидкости на поверхности;',

              'А так же единственным спутником планеты, обладающим плотной атмосферой;',

              'Наконец, он просто красив!',
              ]
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
                                    <h1>Моё предложение: Сатурн</h1>
                                    <h2>Он нас мало интересует;</h2>
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
    elif planet == 'uranus':
        sp = ['Много водички в разных состояниях;',

              'Много спутников на которых тоже можно потусить;',

              'Самый свежий в Солнечной системе;',

              'Наконец, он просто красив!',
              ]
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
                                    <h1>Моё предложение: Уран</h1>
                                    <h2>Там довольно прохладно;</h2>
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
    elif planet == 'neptune':
        def choice_neptune():
            sp = ['То есть можно попробовать надышаться и говорить смешными голосами;',

                  'Быстрые ветры можно поставить кучу ветряков и качать электричество;',

                  'Самый посчитанный в Солнечной системе;',

                  'Наконец, он просто красив!',
                  ]
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
                                    <h1>Моё предложение: Нептун</h1>
                                    <h2>Атмосфера из водорода и гелия;</h2>
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
