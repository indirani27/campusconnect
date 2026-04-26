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
1. Clone the repository:
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
