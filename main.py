from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def render_index():
    data = read_csv_file("./questions.csv")
    return render_template("index.html",questions=data[1],header=data[0])

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f'./questions.csv')
        read_csv_file("./questions.csv")
    return redirect("/")

@app.route("/paste", methods=['POST'])
def read_paste():
    data = request.form.get("data")
    print(data)
    try:
        with open("./questions.csv","wt") as tsv:
            tsv.write(data)
            read_csv_file("./questions.csv")
    except Exception as e:
        print(e)
    return redirect("/")

def read_csv_file(filename):
    header=[]
    questions = [[]]
    try:
        with open(filename) as csvfile:
            data = csv.reader(csvfile)
            header = next(data,[])
            print(header)
            questions = [row for row in data]
    except Exception as e:
        print(e)
    return [header, questions]

if __name__ == "__main__":
    app.run(debug=True)
