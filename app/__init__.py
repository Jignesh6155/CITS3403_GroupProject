from flask import Flask

app = Flask(__name__)

# Configure where uploaded files will be saved
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

# Import routes after creating the app instance to avoid circular imports
from app import routes