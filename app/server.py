from flask import Flask, jsonify, request
import extract_data

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return 'pong'


@app.route('/healthz', methods=['GET'])
def healthz():
    return jsonify({'ok': 'true'})


@app.route('/extract', methods=['POST'])
def extract():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json
        url = body.get('url')
        data = extract_data.convert_pdf_from_url(url)
        return jsonify({'ok': 'true', 'data': data})
    else:
        return jsonify({'ok': 'false', 'error': 'Content-Type must be json'})

def init():
    if __name__ == "server":
        app.run(host='0.0.0.0', port=3000)
