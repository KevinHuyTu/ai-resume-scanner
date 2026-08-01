# AI Resume Scanner

## Overview

The AI Resume Scanner is a Python application that analyzes a PDF resume against a job description by comparing technical skills, calculating a resume match score, and providing personalized recommendations. The project demonstrates PDF processing, text analysis, file handling, and optional AI integration.

This project was developed to simulate the functionality of an Applicant Tracking System (ATS) and help users evaluate how well their resume aligns with a specific job posting.

---

## Features

- Reads resume content directly from a PDF file
- Reads job descriptions from a text file
- Identifies matching skills between the resume and job description
- Identifies missing skills required for the position
- Calculates a resume match score
- Provides a match rating and recommendation
- Supports optional AI-generated feedback (disabled by default)

---

## Technologies Used

- Python
- PyPDF
- File Handling
- String Processing
- Optional OpenAI API Integration
- python-dotenv

---

## Project Structure

```text
ai-resume-scanner/
│
├── resume/
│   └── sample_resume.pdf
│
├── scanner.py
├── job_description.txt
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

## Installation

1. Clone the repository.

2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Place a PDF resume inside the `resume` folder.

4. Paste a job description into `job_description.txt`.

5. Run the application.

```bash
python scanner.py
```

---

## AI Integration

This project includes optional AI integration.

By default:

```python
AI_ENABLED = False
```

No API requests are made while AI is disabled.

To enable AI feedback:

1. Create an OpenAI API key.
2. Store it inside a private `.env` file.
3. Change:

```python
AI_ENABLED = True
```

Your `.env` file is excluded from GitHub using `.gitignore` to keep your API key private.

---

## Example Output

 program output below.

========== AI Resume Scanner ==========

----- Resume Text -----

Kevin Huy Tu 
 (801) 859-xxxx 
kevinxxxxx@icloud.com 
GitHub/Portfolio: github.com/KevinHuyTu 
 
 
EDUCATION 
University of Utah, David Eccles School of Business   Salt Lake City, UT 
Bachelor of Science, Information systems August 2026 
 Honors 
• Opportunity Scholar, selected as a participant in the University of Utah Opportunity Scholars Program, a 
mentorship and academic success program supporting first-generation and underrepresented students. 
 
 Related Coursework 
• Database Management: SQL, MySQL, database design, ERD modeling  
•  Cybersecurity Fundamentals: network security, risk management, defense in depth 
• Cloud Computing: cloud native architecture, containers, CI/CD, serverless computing 
• Data Analytics & Visualization: Tableau, dashboard development, business reporting 
• Systems Analysis & Design: requirements gathering, process modeling, system development lifecycle 
• Web Application Development: Developed web applications using HTML, CSS, JavaScript, Python, 
Django, REST APIs, database integration, and user authentication 
 
 
EXPERIENCE 
FTER’S                                                                                                                                           Salt Lake City, UT 
 Creative Director/ editor/ photographer                                                                                           February 2023  
•  Directed and managed creative campaigns and photoshoots that strengthened brand identity, increased 
audience engagement, and contributed to a sold-out clothing release 
  
7Buddha Tea House                                                                                          Salt Lake City, UT 
Assistant Manager/Team associate   February 2022 – present 
• Led team members in maintaining consistent product knowledge and customer service standards, 
contributing to an efficient and positive customer experience resulting in positive feedback through 
reviews 
• Built strong customer relationships through personalized service, contributing to the retention of 2-3 new 
returning customers per shift  
Nordstrom                                                                                                                        Salt Lake City, UT 
Sales/ Team Member                                                                                      May 2023- July 2023 
• Contributed to strong sales performance in the Men’s Department through exceptional customer service 
and collaboration, helping the department rank among the store’s top performing sections 
• Supported sales and customer satisfaction initiatives that contributed to the store’s high regional 
performance and customer experience metrics 
EOS Fitness                                                                                                                         
                                                                                                                                                      Salt Lake City, UT 
Sales/ Front Desk                                                                              August 2022- January 2023 
• Contributed to the location’s top performing sales results within the state by delivering exceptional 
customer service and promoting membership and training programs 
• Supported membership growth and customer retention efforts, helping drive the location’s ranking among 
the top performing EOS Fitness locations in the state resulting in customer satisfaction through reviews 
and data 
 
 
 
ACTIVITIES TEK Club  July 20 – Present  
• Engaged with industry professionals through networking events, technical workshops, and employer 
presentations to expand knowledge of information technology and career opportunities. 
 
 
Asian American Student Association  August 20 – Present  
• An organization of dedicated and hardworking students within the University of Utah that address social 
issues within all minority groups and spread awareness about different cultures; as well as providing 
opportunities.  
Volunteer Church Representative  August 2021 – present  
• A group of aspiring artists within the University of Utah who target the creative and business aspect of 
photography such as marketing techniques to captivate viewers.  
 
Volunteer Catholic Church Representative   
•  Planned, organized, and taught workshops on goal setting, relationship building, and leadership within 
the Vietnamese catholic community.  
• Teaching assistant at Our Lady of Perpetual Help Catholic Church 
 
 
  

----- Job Description -----

We are seeking a Junior Data Analyst with experience in Python, SQL, Excel, Power BI, Tableau, data visualization, and data analysis.

The ideal candidate should have strong communication and problem-solving skills. Experience with databases, cloud platforms, and dashboard development is preferred.

----- Matching Skills -----

[+] Python
[+] SQL
[+] Tableau

----- Missing Skills -----

[-] Power BI
[-] Excel
[-] Data Analysis

----- Resume Match Score -----
Resume Match Score: 50.0%

----- Match Rating -----

Rating: Low Match
Recommendation: Consider strengthening your resume with more of the required skills.

----- AI Feedback -----

AI analysis is disabled.
Set AI_ENABLED = True to enable personalized AI feedback.
```

---

## Future Improvements

- Export analysis results as a PDF
- Web interface for uploading resumes and job descriptions
- Expanded technical skill database
- AI-generated resume improvement suggestions
- Support for multiple resume formats

---

## Author

Kevin Huy Tu

GitHub:
https://github.com/KevinHuyTu
