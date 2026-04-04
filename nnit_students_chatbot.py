# app.py
# NNIT Student Support Chatbot - Portfolio-ready version

import datetime
import streamlit as st
import joblib

# Load model and vectorizer (make sure these files are in the same folder)
model = joblib.load("chatbot_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Function to generate exam schedule
def get_exam_details(month, start_week):
    """
    Generates exam schedule for a semester.
    Returns:
        first_exam_day
        last_exam_day
        countdown string
        show_days (boolean)
        exam_days (list of weekdays)
    """
    year = datetime.datetime.now().year
    first_day = datetime.date(year, month, 1)
    first_monday = first_day + datetime.timedelta(days=(7 - first_day.weekday()) % 7)  # First Monday
    start_date = first_monday + datetime.timedelta(weeks=start_week - 1)  # Start date for requested week

    exam_days = []
    current_day = start_date
    while len(exam_days) < 10:  # 2 weeks of weekdays
        if current_day.weekday() < 5:
            exam_days.append(current_day)
        current_day += datetime.timedelta(days=1)

    first_exam_day = exam_days[0]
    last_exam_day = exam_days[-1]

    today = datetime.date.today()
    days_to_start = (first_exam_day - today).days
    if days_to_start > 0:
        countdown = f"Exam starts in {days_to_start} days"
        show_days = days_to_start <= 7
    else:
        countdown = ""
        show_days = False

    return first_exam_day, last_exam_day, countdown, show_days, exam_days

# Format exam response
def format_exam_response(start, end, countdown, show_days, days):
    response = f"Exam Schedule:\n {start.strftime('%d %B %Y')} – {end.strftime('%d %B %Y')}."
    if countdown:
        response += f" {countdown}."
    response += " Daily start time: 9:00 AM"

    if show_days:
        day_list = "\n".join([day.strftime("%A, %d %B %Y") for day in days])
        response += f"\n\nExam Days (Weekdays only):\n{day_list}"
    return response

# Generate exam schedules
f_start, f_end, f_count, f_show_days, f_days = get_exam_details(3, 1)  # 1st sem: March, 1st week
s_start, s_end, s_count, s_show_days, s_days = get_exam_details(8, 3)  # 2nd sem: August, 3rd week

# Responses dictionary
responses = {
    "1st Semester exam": format_exam_response(f_start, f_end, f_count, f_show_days, f_days),
    "2nd Semester exam": format_exam_response(s_start, s_end, s_count, s_show_days, s_days),
    "assignment and project deadlines": "Assignment and Project Deadlines:\n- Assignment due: May 25, 2026\n- Project due: June 12, 2026",
    "library": "Library Hours:\n- Weekdays: 8:00 AM – 6:00 PM\n- Weekends: 10:00 AM – 4:00 PM",
    "tutoring": "Tutoring:\n- Tutoring is free.\n- Available subjects: Math, Physics, CS.\n- Next session: May 20, 2026",
    "registration": "Registration:\n- Starts: June 1, 2026\n- Ends: June 15, 2026\n- Add/drop: June 2 – June 6, 2026",
    "counseling": "Counseling:\n- Hours: 8:00 AM – 4:00 PM\n- Days: Mon–Fri\n- Location: Student Affairs Building",
    "attendance_policy": "Attendance Policy:\n- Minimum attendance: 75%\n- Missing class without excuse affects grade",
    "late_submission_policy": "Late Submission:\n- Late work loses 5% per day\n- Extensions require approval",
    "registrar_contact": "Registrar Contact:\n- Email: registrar@university.edu\n- Phone: +234 800 123 4567",
    "support_contact": "Student Support:\n- Email: support@university.edu\n- Office hours: 8:00 AM – 4:00 PM"
}

# Streamlit interface
def run():
    st.header("NNIT Student Support System")
    st.title("📚 Nigerian Navy Institute of Technology: Student Support Chatbot")
    st.write("Ask about exams, assignments, library, registration, etc.")

    user_input = st.text_input("Type your question here:")

    if user_input:
        text = user_input.lower()

        # Rule-based exam detection
        if "exam" in text:
            if any(word in text for word in ["2nd", "second", "sem 2", "semester 2"]):
                intent = "2nd Semester exam"
            elif any(word in text for word in ["1st", "first", "sem 1", "semester 1"]):
                intent = "1st Semester exam"
            else:
                intent = "1st Semester exam"
        else:
            # Fallback to ML model
            input_vec = vectorizer.transform([text])
            intent = model.predict(input_vec)[0]

        answer = responses.get(intent, "Sorry, I don't have an answer for that yet.")
        st.write(f"**Bot:** {answer}")

# Run app
if __name__ == "__main__":
    run()

