from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/info/terms', methods=['GET', 'POST'])
def terms():
    return render_template('terms.html')

@app.route('/info/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html')

@app.route('/info/marketing', methods=['GET', 'POST'])
def age():
    return render_template('marketing.html')

@app.route('/info/total', methods=['GET', 'POST'])
def total():
    return render_template('total.html')

# Chat Route
#@app.route("/prompt", methods=['POST'])
#def prompt():
#    """TOG Prompt Route"""
#    return jsonify(Tog.question_received(request.get_json()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)