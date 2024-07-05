from flask import Flask
from mongo_c import init_mongo

app = Flask(__name__)
init_mongo(app)

if __name__ == "__main__":
    app.run(debug=True, port=5009)
