from flask import Flask, redirect, url_for, render_template, request
from solve import solve

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    board = [['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']]
    if request.method == 'POST' and request.form['submit_button'] == 'Solve':
        data = request
        input = []
        data = request.values
        allowed = ['1','2','3','4','5','6','7','8','9']
        for x in range(9):
            row = []
            for y in range(9):
                cell = data[f'cell-{x}-{y}']
                if cell in allowed:
                    row.append(int(cell))
                else:
                    row.append(0)
            input.append(row)
        board = solve(input)
        return render_template("sudoku.html", board=board)
    return render_template("sudoku.html", board=board)

if __name__ == "__main__":
    app.run()