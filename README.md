# campusconnect
Campus Ambassador Dashboard

Problem Statement
Managing Campus Ambassador programs is often scattered and unstructured. Ambassadors lack recognition, motivation, and a centralized hub.

**CampusConnect** solves this by providing:
- Task workflows with proof submission
- Gamification (points, badges, streaks)
- Dynamic leaderboard
- Profile tracking and recognition

 Tech Stack
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Flask (Python)
- **Templating**: Jinja2

Features
- Task assignment and proof submission
- Leaderboard with points and badges
- Profile page with performance overview
- Connect page with contact info
- About page with program overview and FAQs

Repository Structure
app.py
templates/
   home.html
   tasks.html
   leaderboard.html
   profile.html
   connect.html
   about.html

How to Run Locally

1.Clone the repository:
bash
   git clone https://github.com/yourusername/campusconnect.git
   
2.Navigate to the project folder:
   cd campusconnect
   
3.Install dependencies:
   pip install flask
   
4.Run the app:
   python app.py
   
5.Open in browser:
  http://localhost:5000

Demo video
Watch the demo here:https://drive.google.com/file/d/1Lk9Nct75eFG5D0qP2QGeiS5UkiOHjfYD/view?usp=sharing

Future Enhancements

The current CampusConnect MVP demonstrates core features like task workflows, leaderboard, and badge recognition.  
Planned enhancements include:
- Gamification Expansion: Add streak tracking, tiered badges, and reward redemption.
- Analytics Dashboard: Provide insights into ambassador performance, task completion rates, and engagement trends.
- Integration Options: Future scope to connect with Google Drive/Docs for proof submissions.
- AI‑Driven Insights: Predictive analysis of ambassador activity to suggest personalized tasks.
