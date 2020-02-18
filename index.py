#workon venv // deactivate
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/contrataciones')
def contrataciones():
    return render_template('contrataciones.html')

if __name__ == '__main__':
    app.run(debug=True)
