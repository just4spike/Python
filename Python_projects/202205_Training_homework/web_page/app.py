from flask import Flask
from views import views # imports views from views.py

app = Flask(__name__) # initializes the application
app.register_blueprint(views, url_prefix="/")

if __name__=='__main__':
    app.run(debug=True) #, port=5000) # Port 5000 by default