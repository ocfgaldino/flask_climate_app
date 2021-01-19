from flask import Flask 
from climate.ext.site.main import bp 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    
    return app