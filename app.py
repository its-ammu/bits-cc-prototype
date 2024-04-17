from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/s3Encryption')
def s3Encryption():
    return render_template('s3Encryption.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}! Your form has been submitted successfully."

if __name__ == '__main__':
    app.run(debug=True)
