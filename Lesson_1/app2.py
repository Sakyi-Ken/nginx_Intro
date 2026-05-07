from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return {'message': 'Direct Flask access', 'headers': dict(request.headers)} 

@app.route('/users')
def users():
    return {'users': ['Alice', 'Bob', 'Charlie']}

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3002)