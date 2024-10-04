from flask import Flask, request
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
import os
import logging

app = Flask(__name__)

# Enable CSRF protection
csrf = CSRFProtect(app)

# Rate limiting
limiter = Limiter(app, key_func=get_remote_address)

@app.after_request
def set_secure_cookie(response):
    response.set_cookie('session_id', 'your-session-id', secure=True, httponly=True)
    return response

@app.after_request
def add_csp_header(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

@app.errorhandler(404)
def not_found(error):
    return {'message': 'Resource not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    return {'message': 'Internal Server Error'}, 500

@app.route('/api', methods=['GET'])
@limiter.limit("5 per minute")
def api_endpoint():
    logging.info('API endpoint accessed')
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))
