from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None, value=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        value = request.form.get('value', type=float)
        if value is None:
            return render_template('index.html', result=None, value=None, error='Veuillez entrer un chiffre valide')
        
        result = {
            'Lu': round(value * 0.27, 2),
            'San': round(value * 0.28, 2),
            'Hel': round(value * 0.45, 2)
        }
        return render_template('index.html', result=result, value=value, error=None)
    except Exception as e:
        return render_template('index.html', result=None, value=None, error=str(e))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
