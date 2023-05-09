from locust import HttpUser, TaskSet, task, between

"""
Para ejecutar los tests de carga:
    1. Vaciar tablas de la base de datos
    2. Para poblarla con datos estáticos, ejecutar el siguiente comando: python manage.py loaddata "fixtures/initial.json"
"""

HOST = "https://sarandonga3.pythonanywhere.com"


class DefHome(TaskSet):
    @task
    def home(self):
        self.client.get("")


class DefLogin(TaskSet):
    @task
    def login(self):
        self.client.get("/login")

    @task
    def login_post(self):
        payload = {"username": "admin@videssur.com", "password": "admin"}
        self.client.post("/login", data=payload)


class DefStock(TaskSet):
    @task
    def stock(self):
        self.client.get("/stock/list")

    @task
    def stock_post(self):
        payload = {
            "name": "Test",
            "model": "Test",
            "quantity": 100,
            "amount": 67,
            "notes": "This is a create stock test from locust",
        }
        self.client.post("/stock/create", data=payload)


class Home(HttpUser):
    host = HOST
    tasks = [DefHome]
    wait_time = between(3, 5)


class Login(HttpUser):
    host = HOST
    tasks = [DefLogin]
    wait_time = between(3, 5)
