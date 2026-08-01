import os

from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

AI_ENABLED = False

load_dotenv()

print("========== AI Resume Scanner ==========")

reader = PdfReader("resume/sample_resume.pdf")

resume_text = ""

for page in reader.pages:
    resume_text += page.extract_text()

print("\n----- Resume Text -----\n")

print(resume_text)

with open("job_description.txt", "r", encoding="utf-8") as job_files:
    job_description = job_files.read()

print("\n----- Job Description -----\n")

print(job_description)

skills = [
    "Python",
    "SQL",
    "Power BI",
    "Tableau",
    "Excel",
    "Django",
    "MySQL",
    "JavaScript",
    "HTML",
    "CSS",
    "Data Analysis",
    "Cybersecurity"
]

matching_skills = []
missing_skills = []

for skill in skills:
    skill_in_resume = skill.lower() in resume_text.lower()
    skill_in_job = skill.lower() in job_description.lower()

    if skill_in_resume and skill_in_job:
        matching_skills.append(skill)

    elif skill_in_job and not skill_in_resume:
        missing_skills.append(skill)

print("\n----- Matching Skills -----\n")

for skill in matching_skills:
    print(f"[+] {skill}")

print("\n----- Missing Skills -----\n")

for skill in missing_skills:
    print(f"[-] {skill}")

if len(matching_skills) + len(missing_skills) > 0:
     match_score = (
        len(matching_skills)
        / (len(matching_skills) + len(missing_skills))
    ) * 100
else:
        match_score = 0

print("\n----- Resume Match Score -----")

print(f"Resume Match Score: {match_score:.1f}%")

print("\n----- Match Rating -----\n")

if match_score >= 80:
    print("Rating: Strong Match")
    print("Recommendation: your resume aligns well with this job description.")

elif match_score >= 60:
    print("Rating: Moderate Match")
    print("Recommendation: Your resume matches many requirements, but some important skills are missing.")

else:
     print("Rating: Low Match")
     print("Recommendation: Consider strengthening your resume with more of the required skills.")

def generate_ai_feedback(resume, job, matching, missing):
    api_key = os.getenv("OPEN_AI_KEY")

    if not api_key:
        return "AI feedback unavailable: no API key was found."

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are reviewing a resume against a job description.

Provide concise, honest feeedback using these headings:
1. Strengths
2. Gaps
3. Recommended Resume Imporvements

Do not invent experience or recommend adding skills the candidate does not have.
Only suggest emphasizing truthful experience already show in the resume.

Matching skills:
{",".join(matching) if matching else "None identified"}

Missing skills:
{",".join(missing) if missing else "None identified"}

Resume:
{resume}

Job description:
{job}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text

print("\n----- AI Feedback -----\n")

if AI_ENABLED:
    try:
        ai_feedback = generate_ai_feedback(
            resume_text,
            job_description,
            matching_skills,
            missing_skills
        )
        print(ai_feedback)

    except Exception as error:
        print(f"AI feedback could not be generated: {error}")

else:
    print("AI analysis is disabled.")
    print("Set AI_ENABLED = True to enable personalized AI feedback.")

    