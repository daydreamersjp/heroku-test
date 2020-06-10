from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World! Check auto-update."
    
if __name__=="__main__":
    app.run()