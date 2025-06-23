from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Built-in habit suggestions (30 habits)
HABIT_SUGGESTIONS = [
    "Drink 8 glasses of water",
    "Read for 30 minutes",
    "Exercise for 30 minutes",
    "Meditate for 10 minutes",
    "Write in a journal",
    "Take a walk outside",
    "Eat a healthy breakfast",
    "Practice gratitude",
    "Learn something new",
    "Call a friend or family member",
    "Stretch for 15 minutes",
    "Listen to a podcast",
    "Organize your workspace",
    "Take deep breaths",
    "Limit screen time",
    "Prepare meals in advance",
    "Practice a hobby",
    "Get 7-8 hours of sleep",
    "Spend time in nature",
    "Do a random act of kindness",
    "Practice positive self-talk",
    "Declutter one area of your home",
    "Take vitamins or supplements",
    "Practice a musical instrument",
    "Do a crossword or puzzle",
    "Plan tomorrow's tasks",
    "Drink green tea",
    "Do 50 push-ups or squats",
    "Watch an educational video",
    "Practice a new language"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_tracking():
    name = request.form.get('name', '').strip()
    if not name:
        return redirect(url_for('index'))
    
    # Store user name in session
    session['user_name'] = name
    
    # Randomly select 10 habits
    selected_habits = random.sample(HABIT_SUGGESTIONS, 10)
    session['selected_habits'] = selected_habits
    session['completed_habits'] = []
    
    return redirect(url_for('tracker'))

@app.route('/tracker')
def tracker():
    if 'user_name' not in session:
        return redirect(url_for('index'))
    
    user_name = session['user_name']
    habits = session.get('selected_habits', [])
    completed = session.get('completed_habits', [])
    
    return render_template('tracker.html', 
                         user_name=user_name, 
                         habits=habits, 
                         completed=completed)

@app.route('/toggle_habit', methods=['POST'])
def toggle_habit():
    habit = request.form.get('habit')
    completed = session.get('completed_habits', [])
    
    if habit in completed:
        completed.remove(habit)
    else:
        completed.append(habit)
    
    session['completed_habits'] = completed
    return redirect(url_for('tracker'))

@app.route('/summary')
def summary():
    if 'user_name' not in session:
        return redirect(url_for('index'))
    
    user_name = session['user_name']
    total_habits = len(session.get('selected_habits', []))
    completed_count = len(session.get('completed_habits', []))
    
    # Generate motivational message based on completion rate
    completion_rate = (completed_count / total_habits * 100) if total_habits > 0 else 0
    
    if completion_rate == 100:
        message = "🎉 Perfect! You're absolutely crushing it! Every habit completed!"
    elif completion_rate >= 80:
        message = "🌟 Amazing work! You're building incredible momentum!"
    elif completion_rate >= 60:
        message = "💪 Great progress! You're developing strong habits!"
    elif completion_rate >= 40:
        message = "👍 Good start! Keep building those positive routines!"
    elif completion_rate >= 20:
        message = "🌱 Every step counts! You're on the right path!"
    else:
        message = "🚀 Tomorrow is a fresh start! You've got this!"
    
    return render_template('summary.html',
                         user_name=user_name,
                         completed_count=completed_count,
                         total_habits=total_habits,
                         completion_rate=int(completion_rate),
                         message=message)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)