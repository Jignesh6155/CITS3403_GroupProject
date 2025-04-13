import os
from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return render_template('results.html', data=None)

    if 'resume' not in request.files:
        return redirect(url_for('index'))

    resume_file = request.files['resume']
    
    if resume_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
        resume_file.save(file_path)
    else:
        file_path = None

    preferences = request.form.getlist('preferences[]')
    company = request.form.get('company', '')

    data = {
        'preferences': preferences,
        'company': company,
        'filename': resume_file.filename if resume_file.filename != '' else None
    }

    return render_template('results.html', data=data)
