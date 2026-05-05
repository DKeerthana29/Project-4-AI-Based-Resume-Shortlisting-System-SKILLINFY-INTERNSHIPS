import os
import csv
import json
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from nlp_utils import extract_text, calculate_similarity, extract_skills, generate_ats_metrics

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Needed for flashing messages

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
CSV_PATH = os.path.join(UPLOAD_FOLDER, 'export.csv')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_description = request.form.get('job_description', '')
        
        # Check if files were uploaded
        if 'resumes' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
        
        files = request.files.getlist('resumes')
        
        if not files or files[0].filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        
        if not job_description.strip():
            flash('Job description is required', 'error')
            return redirect(request.url)

        candidates = []
        resumes_text = []
        filenames = []
        
        # Save files and extract text
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                
                text = extract_text(file_path)
                resumes_text.append(text)
                filenames.append(filename)
                
        if resumes_text:
            scores = calculate_similarity(job_description, resumes_text)
            
            # Combine filenames, text, and scores
            for i in range(len(filenames)):
                extracted_skills = extract_skills(resumes_text[i])
                ats_data = generate_ats_metrics(resumes_text[i], job_description, scores[i])
                
                candidates.append({
                    'id': i,
                    'filename': filenames[i],
                    'score': ats_data['ats_score'],
                    'semantic_score': ats_data['semantic_score'],
                    'text_snippet': resumes_text[i][:200] + "..." if len(resumes_text[i]) > 200 else resumes_text[i],
                    'skills': extracted_skills,
                    'ats_data': ats_data,
                    'radar_data': json.dumps(ats_data['radar_data'])
                })
                
            # Rank candidates by score descending
            candidates.sort(key=lambda x: x['score'], reverse=True)
            
            # Save to CSV for exporting
            with open(CSV_PATH, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Rank', 'Filename', 'Overall ATS %', 'Semantic %', 'Email', 'Phone', 'Word Count', 'Action Verbs']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for rank, c in enumerate(candidates, 1):
                    writer.writerow({
                        'Rank': rank,
                        'Filename': c['filename'],
                        'Overall ATS %': c['score'],
                        'Semantic %': c['semantic_score'],
                        'Email': c['ats_data'].get('email', 'N/A'),
                        'Phone': c['ats_data'].get('phone', 'N/A'),
                        'Word Count': c['ats_data'].get('word_count', 0),
                        'Action Verbs': c['ats_data'].get('action_verbs_found', 0)
                    })
            
        return render_template('results.html', candidates=candidates, jd=job_description)

    return render_template('index.html')

@app.route('/export')
def export_csv():
    from flask import send_file
    if os.path.exists(CSV_PATH):
        return send_file(CSV_PATH, as_attachment=True, download_name='ats_shortlist.csv')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
