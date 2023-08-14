from flask import Flask
from flask import jsonify
import pdf_reader

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    data = pdf_reader.convert()
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
