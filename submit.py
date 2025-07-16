from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    print(f"Name: {name}")
    print(f"Email: {email}")
    return f"<h3>Received:</h3><p>Name: {name}</p><p>Email: {email}</p>"

if __name__ == '__main__':
    app.run(debug=True)