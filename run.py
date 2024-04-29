from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/info/terms', methods=['GET', 'POST'])
def terms():
    return render_template('terms.html')

@app.route('/info/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html')

@app.route('/info/age', methods=['GET', 'POST'])
def age():
    return render_template('age.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)