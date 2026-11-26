from fastapi import FastAPI

app = FastAPI()

feedbacks = [
    "Excellent service",
    "Fast delivery",
    "Friendly support"
]

products = [
    "Laptop",
    "Keyboard",
    "Mouse"
]


@app.get("/")
def home():

    return {
        "message": "Hello from FastAPI"
    }


@app.get("/student")
def get_student():
    return {
        "id": 101,
        "name": "Arun",
        "age": 22,
        "course": "Python"
    }


@app.get("/welcome")
def welcome():
    return {
        "message": "Welcome to the Home Page"
    }


@app.get("/student/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id,
        "message": "Student details retrieved"
    }


@app.get("/products")
def get_products(category: str, price: int, color: str):
    return {
        "category": category,
        "price": price,
        "color": color
    }


@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):

    return {
        "a": a,
        "b": b,
        "result": a+b
    }


@app.get("/subtract")
def subtract_numbers(a: int, b: int):

    return {
        "a": a,
        "b": b,
        "result": a-b
    }


@app.get("/evenorodd/{number}")
def even_or_odd(number: int):
    if number % 2 == 0:
        return {
            number: number,
            'result': "Even"
        }
    else:
        return {
            number: number,
            'result': "Odd"
        }


@app.get("/feedbacks")
def get_feedback():
    return feedbacks


@app.get("/productList")
def get_product_list():
    return products
