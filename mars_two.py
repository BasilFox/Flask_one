from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<profil>')
def training(profil):
    return render_template('train.html', prof=profil)


@app.route('/list_prof/<sp>')
def spisok(sp):
    spec = ['Инженер-исследователь', 'Пилот', 'Строитель', 'Экзобиолог',
            'Инженер по терраформированию', 'Климатолог', 'Специалист по радиационной защите',
            'Астрогеолог', 'Гляциолог', 'Инженер жизнеобеспечения', 'Метеоролог',
            'Оператор марсохода', 'Киберинженер', 'Штурман', 'Пилот дронов']
    return render_template('professions.html', list=sp, spec=spec)


@app.route('/auto_answer')
def otvet():
    anketa = {'surname': 'Иванов',
              'name': 'Иван',
              'education': 'Высшее',
              'profession': 'Геолог',
              'sex': 'Мужской',
              'motivation': 'Захотелось',
              'ready': 'Готов'}
    return render_template('autoanswer.html', **anketa)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
