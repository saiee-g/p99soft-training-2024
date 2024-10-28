from flask import Flask, request, Response
import json


app = Flask(__name__) #initialize

@app.route('/cats')
def cats():

    cat_list = [
        "Cat's List",
        {
            "breed": "black",
            "name": "bubbletea",
            "age": 3
        },
        {
           "breed": "white",
            "name": "cupcake",
            "age": 4 
        },
        {
            "breed": "ginger",
            "name": "ron",
            "age": 11
        },
        {
            "breed": "tabby",
            "name": "minerva",
            "age": 22
        }
    ]
    return Response(json.dumps(cat_list), mimetype='application/json')
    

@app.route("/")
def greet():
    return "Meowwww"


if __name__ == "__main__":
    app.run(Debug = True)