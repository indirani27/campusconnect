from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

# Tasks Page
@app.route("/tasks")
def tasks():
    # Example static tasks (can be replaced with dynamic later)
    tasks = [
        {"title": "Promote Hackathon Event", "description": "Share poster on Instagram", "completed": False},
        {"title": "Referral Task", "description": "Refer 3 friends to register", "completed": True},
    ]
    return render_template("tasks.html", tasks=tasks)

# Add Task Page
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        user = request.form.get("user")

        # For now, just print to console (no DB)
        print(f"New Task Added: {title}, {description}, assigned to {user}")

        return redirect(url_for("tasks"))

    return render_template("add_task.html")

# Leaderboard Page
@app.route("/leaderboard")
def leaderboard():
    leaders = [
        {"rank": 1, "name": "Indirani", "points": 120, "badges": ["Top Performer", "7-Day Streak"]},
        {"rank": 2, "name": "Rahul", "points": 95, "badges": ["Referral Champ"]},
        {"rank": 3, "name": "Sneha", "points": 80, "badges": ["Content Creator"]}
    ]
    return render_template("leaderboard.html", leaders=leaders)

# Connect Page
@app.route("/connect")
def connect():
    return render_template("connect.html")

# Profile Page
@app.route("/profile")
def profile():
    profile_data = {
        "points": 120,
        "badges": ["Top Performer", "7-Day Streak", "Referral Champ"],
        "tasks": ["Promoted Hackathon Event", "Referred 3 Friends", "Created LinkedIn Post"]
    }
    return render_template("profile.html", profile=profile_data)

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
