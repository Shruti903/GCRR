from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/recipe')
def recipes():
    return render_template('recipe.html')

@app.route('/starthere')
def starthere():
    return render_template('starthere.html')

@app.route('/viewall')
def viewall():
    return render_template('viewall.html')

if __name__ == '__main__':
    app.run(debug=True)
