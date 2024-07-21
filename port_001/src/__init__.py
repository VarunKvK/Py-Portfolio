from flask import render_template,Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app