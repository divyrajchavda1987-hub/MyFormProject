from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    village = request.form['village']

    with open("data.txt", "a") as f:
        f.write(f"{first_name} {last_name}, Age: {age}, Village: {village}\n")

    return "✅ Data saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)