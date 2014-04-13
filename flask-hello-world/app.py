# ---- Flask Hello world ---- #
# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url


@app.route('/')
@app.route('/hello')
def hello_world():
    return "Hello world"

# start the development server using the run method
if __name__ == "__main__":
    app.run()
