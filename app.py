from flask import Flask, render_template

app = Flask(__name__)

# ── Edit your resume data here ──────────────────────────────────────────────

RESUME = {
    "name": "Your Name",
    "title": "Software Engineer",
    "email": "you@email.com",
    "phone": "+1 (555) 000-0000",
    "location": "Mumbai, India",
    "linkedin": "linkedin.com/in/yourprofile",
    "github": "github.com/yourusername",
    "summary": (
        "Passionate software engineer with experience building scalable "
        "web applications. I love clean code, thoughtful design, and "
        "solving hard problems with simple solutions."
    ),
    "experience": [
        {
            "company": "Tech Company",
            "role": "Senior Software Engineer",
            "period": "Jan 2022 – Present",
            "location": "Mumbai, India",
            "points": [
                "Led development of a microservices platform serving 2M+ users.",
                "Reduced API latency by 40% through caching and query optimization.",
                "Mentored a team of 4 junior engineers.",
            ],
        },
        {
            "company": "Startup Inc.",
            "role": "Software Engineer",
            "period": "Jun 2019 – Dec 2021",
            "location": "Pune, India",
            "points": [
                "Built and shipped 3 full-stack product features end-to-end.",
                "Integrated third-party payment and analytics APIs.",
                "Improved test coverage from 45% to 85%.",
            ],
        },
    ],
    "education": [
        {
            "school": "University of Mumbai",
            "degree": "B.E. Computer Engineering",
            "period": "2015 – 2019",
            "detail": "GPA 8.7 / 10",
        }
    ],
    "skills": {
        "Languages": ["Python", "JavaScript", "TypeScript", "SQL"],
        "Frameworks": ["Flask", "FastAPI", "React", "Node.js"],
        "Tools": ["Docker", "Git", "PostgreSQL", "Redis", "AWS"],
    },
    "projects": [
        {
            "name": "OpenReview",
            "description": "A peer-review platform for academic papers built with Flask and React.",
            "link": "github.com/yourusername/openreview",
        },
        {
            "name": "BudgetBot",
            "description": "CLI expense tracker with Python that syncs to Google Sheets.",
            "link": "github.com/yourusername/budgetbot",
        },
    ],
}

# ────────────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html", r=RESUME)

if __name__ == "__main__":
    app.run(debug=True)
