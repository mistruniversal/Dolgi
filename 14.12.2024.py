"""FLASK"""
1
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет, добро пожаловать на главную страницу!"

@app.route('/about')
def about():
    return "Это приложение создано для демонстрации работы с Flask."

if __name__ == '__main__':
    app.run(debug=True)





2
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return f"Ваше имя: {name}, Ваш возраст: {age}"
    return '''
        <form method="post">
            Имя: <input type="text" name="name"><br>
            Возраст: <input type="text" name="age"><br>
            <input type="submit" value="Отправить">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)




3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_title = request.form['task']
        new_task = Task(title=task_title)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))

    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:task_id>')
def delete(task_id):
    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()  # Создание базы данных
    app.run(debug=True)



"""FastAPI"""
1
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Привет, добро пожаловать на главную страницу!</h1>"

@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello(name: str):
    return f"<h1>Привет, {name}!</h1>"


2
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/")
async def submit_form(name: str = Form(...), age: int = Form(...)):
    return f"Ваше имя: {name}, Ваш возраст: {age}"



3
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("weather.html", {"request": request})

@app.post("/")
async def submit_city(city: str = Form(...)):
    # Здесь можно добавить логику для получения информации о погоде
    weather_info = f"Погода в городе {city}: солнечно!"  # Заглушка
    return weather_info






4
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

tasks = []

@app.get("/", response_class=HTMLResponse)
async def read_tasks(request: Request):
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks})

@app.post("/")
async def add_task(task: str = Form(...)):
    tasks.append(task)
    return {"message": "Задача добавлена!"}
