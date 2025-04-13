import os
from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    # Check if the 'resume' file part is present in the request
    if 'resume' not in request.files:
        # Optionally, you could flash a message here to tell the user
        return redirect(url_for('index'))
    
    resume_file = request.files['resume']
    
    # Save the file if provided and has a valid filename.
    if resume_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
        resume_file.save(file_path)
    else:
        file_path = None

    # Retrieve checkbox preferences
    preferences = request.form.getlist('preferences[]')
    
    # Retrieve company (optional) text input
    company = request.form.get('company', '')
    
    # Bundle data to pass to the results template
    data = {
        'preferences': preferences,
        'company': company,
        'filename': resume_file.filename if resume_file.filename != '' else None
    }
    #
    return render_template('results.html', data=data)