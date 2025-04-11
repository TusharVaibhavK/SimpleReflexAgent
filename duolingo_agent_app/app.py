from flask import Flask, render_template, request

app = Flask(__name__)


def duolingo_agent(lesson_done_today, has_streak, last_session_mistake):
    if not lesson_done_today:
        return "📚 Prompt to do today’s lesson"
    elif not has_streak:
        return "🔥 Encourage to start a streak"
    elif last_session_mistake:
        return "🧠 Suggest a practice session"
    else:
        return "✅ Great job! Keep going!"


@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    if request.method == 'POST':
        lesson_done_today = request.form.get('lesson_done') == 'yes'
        has_streak = request.form.get('streak') == 'yes'
        last_session_mistake = request.form.get('mistake') == 'yes'
        response = duolingo_agent(
            lesson_done_today, has_streak, last_session_mistake)
    return render_template('index.html', response=response)


if __name__ == '__main__':
    app.run(debug=True)
