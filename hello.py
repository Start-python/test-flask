from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def hello():
    html = render_template('index.html', a = 'これは変数です')
    return html
 
if __name__ == "__main__":
    app.run()