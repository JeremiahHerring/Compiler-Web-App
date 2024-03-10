from flask import Blueprint, render_template, request
from LexerFSM.main import lexer

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route("/lexical-analyzer", methods=['GET', 'POST'])
def lexical_analyer():
    if request.method == 'POST':
        if 'textareaInput' in request.form:
            code = request.form['textareaInput']
            results = lexer(code)
            return render_template("lexical-analyzer-results.html", results=results)
        else:
            return "Error: 'textareaInput' not found in form data", 400

    return render_template("lexical-analyzer.html")

@views.route('lexical-analyzer-results', methods=['GET'])
def lexical_analyzer_results():
    return render_template('lexical-analyzer-results')

@views.route("/syntax-analyzer")
def syntax_analyer():
    return render_template("syntax-analyzer.html")
