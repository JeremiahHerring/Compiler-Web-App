from flask import Blueprint, render_template, request, session
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

            # Store the results in a session
            session['lexical_results'] = results

            return render_template("lexical-analyzer-results.html", results=results)
        else:
            return "Error: 'textareaInput' not found in form data", 400

    return render_template("lexical-analyzer.html")

@views.route('lexical-analyzer-results', methods=['GET'])
def lexical_analyzer_results():
    # Retrieve the results from the session
    results = session.pop('lexical_results', None)

    if results is not None:
        return render_template('lexical-analyzer-results.html', results=results)
    else:
        return "Error: Results not found in session", 400
    

@views.route("/syntax-analyzer")
def syntax_analyer():
    return render_template("syntax-analyzer.html")
