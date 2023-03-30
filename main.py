from flask import Flask

app = Flask(__name__)

# employee

# view  cv
@app.route("/cv/", methods=['GET'])
def cv():
    pass

# see and edit skill and technolgy name
@app.route("/technology", methods=['GET', 'POST'])
def technology():
    pass

# see and edit expiriance
@app.route("/expiriance ", methods=['GET', 'POST'])
def expiriance():
    pass

# staff and admin

@app.route("/user/<username>/cv", methods=['GET'])
def user_cv():
    pass

@app.route("/static/count", methods=['GET'])
def user_cv():
    technology = request.args.get('technology', None)
    skill = request.args.get('skill', None)
    pass