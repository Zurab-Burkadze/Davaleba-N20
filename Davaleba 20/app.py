from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/films')
def films():
    films = ['Harry Potter and Philosophers Stone', 'Harry Potter and Chamber of Secrets', 'Harry Potter and Prisoner of Azkaban', 'Harry Potter and Goblet of Fire', 'Harry Potter and Order of the Phoenix', 'Harry Potter and Half-Blood Prince', 'Harry Potter and Deathly Hallows']
    return render_template('films.html', films=films)

if __name__ == '__main__':
    app.run(debug=True)