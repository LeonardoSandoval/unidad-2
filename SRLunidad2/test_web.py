from formulas import Densi, Area
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', titulo='Densidad de Material')


@app.route('/exe_densidad', methods=['GET', 'POST'])
def execute() -> 'html':
    m = int(request.form['m'])
    v = int(request.form['v'])
    title = 'Esta es la Densidad:'
    result = Densi(m, v)
    return render_template('result.html',
                           the_title=title,
                           the_m=m,
                           the_v=v,
                           the_result=result, )


if __name__ == '__main__':
    app.run('localhost', 5001, debug=True)
