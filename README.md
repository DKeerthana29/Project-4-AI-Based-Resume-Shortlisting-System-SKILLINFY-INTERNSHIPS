# Project-4-AI-Based-Resume-Shortlisting-System-SKILLINFY-INTERNSHIPS
Developing a tool to shortlist resumes based on job descriptions using NLP and ranking algorithms.


# AI-Based Resume Shortlisting System

## Project Description
The **AI-Based Resume Shortlisting System** is an intelligent recruitment automation tool that analyzes resumes and matches them against job descriptions using **Natural Language Processing (NLP)** and ranking algorithms.

The system extracts relevant candidate skills, compares them with job requirements, calculates similarity scores, and ranks applicants based on their suitability for the role.

This project demonstrates how Artificial Intelligence can streamline the recruitment process by automating resume screening and reducing manual effort.

---

## Objective
The primary objective of this project is to build an AI-powered resume screening system that can:

- Parse resumes automatically
- Extract important skills and information
- Match resumes with job descriptions
- Score candidates based on relevance
- Rank applicants for shortlisting

---

## Features

### Resume Parsing
Extracts text from resumes.

### Skill Extraction
Identifies candidate skills using NLP.

### Job Description Analysis
Processes job requirements.

### Similarity Matching
Compares resume content with job descriptions.

### Candidate Scoring
Assigns matching scores.

### Ranking System
Ranks candidates from most suitable to least suitable.

### Automated Shortlisting
Reduces manual HR workload.

---

## Technologies Used

- **Python**
- **Natural Language Processing (NLP)**
- **Scikit-learn**
- **spaCy / NLTK**
- **TF-IDF Vectorization**
- **Cosine Similarity**
- **Pandas**
- **PDF/Text Parsing Libraries**

---

## Concepts & Skills Learned

This project covers:

- Named Entity Recognition (NER)
- Text Parsing
- Resume Information Extraction
- TF-IDF Vectorization
- Cosine Similarity
- Candidate Ranking Algorithms
- Recruitment Automation

---

## System Workflow

### Step 1: Input Collection
The system receives:

- Resume files
- Job description

---

### Step 2: Resume Parsing
Text is extracted from uploaded resumes.

Supported formats:

- PDF
- TXT
- DOCX

---

### Step 3: Text Preprocessing
The extracted text is cleaned using:

- Lowercasing
- Tokenization
- Stopword removal
- Lemmatization

---

### Step 4: Skill Extraction
Important skills are identified using NLP.

Examples:

- Python
- Machine Learning
- SQL
- Data Analysis

---

### Step 5: Job Description Analysis
The system extracts required skills from the job description.

---

### Step 6: Similarity Calculation
Resume content is compared with job description using:

- TF-IDF Vectorization
- Cosine Similarity

---

### Step 7: Candidate Scoring
Each resume gets a matching score.

---

### Step 8: Ranking
Candidates are ranked in descending order of suitability.

---

## Project Structure

```plaintext
AI-Resume-Shortlisting-System/
│
├── resumes/
│   ├── candidate1.pdf
│   ├── candidate2.pdf
│
├── data/
│   └── job_description.txt
│
├── src/
│   ├── parser.py
│   ├── preprocess.py
│   ├── similarity.py
│   ├── ranking.py
│
├── output/
│   └── shortlisted_candidates.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation Guide

### Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Shortlisting-System.git
```

---

### Navigate to Project Folder

```bash
cd AI-Resume-Shortlisting-System
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Start the System

```bash
python app.py
```

---

## How It Works

### Upload Resumes
Place candidate resumes in the resumes folder.

---

### Add Job Description
Save job requirements in the data folder.

---

### Run Matching Engine
The system processes resumes.

---

### View Results
Shortlisted candidates are ranked automatically.

---

## Sample Output

| Candidate Name | Matching Score | Rank |
|---------------|---------------|------|
| John Doe | 92% | 1 |
| Alice Smith | 87% | 2 |
| David Lee | 81% | 3 |

---

## NLP Techniques Used

### TF-IDF Vectorization
Converts text into numerical vectors.

Purpose:
Measure term importance.

---

### Cosine Similarity
Measures similarity between resume and job description.

Formula:

Cosine Similarity = (A · B) / (||A|| × ||B||)

---

### Named Entity Recognition (NER)
Extracts:

- Skills
- Education
- Certifications
- Experience

---

## Future Enhancements

This project can be improved by adding:

### Deep Learning Models
Use BERT for contextual matching.

---

### Web Dashboard
Interactive recruiter dashboard.

---

### Cloud Storage
Store resumes securely.

---

### Advanced Analytics
Generate hiring insights.

---

### Mobile Accessibility
Access via mobile app.

---

### Interview Recommendation
Automatically suggest interview candidates.

---

## Learning Outcomes

Through this project, you will learn:

- NLP for document processing
- Resume parsing
- Similarity algorithms
- Ranking systems
- Recruitment automation using AI

---

## Applications

This system can be used in:

- HR Departments
- Recruitment Agencies
- Job Portals
- Campus Placement Cells
- Corporate Hiring Systems

---

## Challenges Faced

Some common challenges include:

- Different resume formats
- Parsing PDF text accurately
- Skill extraction complexity
- Context understanding limitations

---

## Contribution

Contributions are welcome.

Steps:

1. Fork repository
2. Create branch
3. Make changes
4. Submit pull request

---

## License

This project is developed for **educational and academic purposes**.

---

## Acknowledgement

Developed as part of an academic AI project to demonstrate intelligent recruitment automation using Natural Language Processing.

---

## Author

**Dondluru Keerthana**  
B.Tech CSE (AI)  
Amrita Vishwa Vidyapeetham
