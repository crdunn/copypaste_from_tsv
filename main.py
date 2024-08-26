from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

header = []
questions = [[]]

@app.route("/")
def render_index():
    return render_template("index.html",questions=questions,header=header)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f'./questions.csv')
        read_csv_file("./questions.csv")
    return redirect("/")

def read_csv_file(filename):
    global header
    global questions
    try:
        with open(filename) as tsv:
            data = csv.reader(tsv,delimiter="\t")
            header = next(data,None)
            questions = [row for row in data][1:]
    except:
        print("No document")
    

if __name__ == "__main__":
    read_csv_file("./questions.csv")
    app.run(debug=True)