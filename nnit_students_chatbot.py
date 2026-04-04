import datetime
import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("chatbot_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Helper functions
def get_exam_details(month, start_week):
    year = datetime.datetime.now().year
    first_day = datetime.date(year, month, 1)
    first_monday = first_day + datetime.timedelta(days=(7 - first_day.weekday()) % 7)
    start_date = first_monday + datetime.timedelta(weeks=start_week - 1)
    
    exam_days = []
    current_day = start_date
    while len(exam_days) < 10:
        if current_day.weekday() < 5:
            exam_days.append(current_day)
        current_day += datetime.timedelta(days=1)
    
    first_exam_day = exam_days[0]
    last_exam_day = exam_days[-1]

    today = datetime.date.today()
    days_to_start = (first_exam_day - today).days
    countdown = f"Exam starts in {days_to_start} days" if days_to_start > 0 else ""
    show_days = 0 < days_to_start <= 7
    return first_exam_day, last_exam_day, countdown, show_days, exam_days

def format_exam_response(start, end, countdown, show_days, days):
    response = f"Exam Schedule:\n {start.strftime('%d %B %Y')} – {end.strftime('%d %B %Y')}."
    if countdown:
        response += f" {countdown}."
    response += " Daily start time: 9:00 AM"
    if show_days:
        day_list = "\n".join([day.strftime("%A, %d %B %Y") for day in days])
        response += f"\n\nExam Days (Weekdays only):\n{day_list}"
    return response

# Main function to run the app
def run():
    st.header("NNIT Student Support System")
    st.write("Ask about exams, assignments, library, registration, etc.")
    
    # Determine upcoming semester
    today = datetime.date.today()
    if today.month <= 6:
        f_start, f_end, f_count, f_show_days, f_days = get_exam_details(3, 1)
        upcoming_semester = "1st Semester exam"
    else:
        s_start, s_end, s_count, s_show_days, s_days = get_exam_details(8, 3)
        upcoming_semester = "2nd Semester exam"

    # Build responses
    responses = {}
    if today.month <= 6:
        responses["1st Semester exam"] = format_exam_response(f_start, f_end, f_count, f_show_days, f_days)
    else:
        responses["2nd Semester exam"] = format_exam_response(s_start, s_end, s_count, s_show_days, s_days)
    
    responses.update({
        "assignment and project deadlines": "Assignment and Project Deadlines:\n- Assignment due: May 25, 2026\n- Project due: June 12, 2026",
        "library": "Library Hours:\n- Weekdays: 8:00 AM – 6:00 PM\n- Weekends: 10:00 AM – 4:00 PM",
        "tutoring": "Tutoring:\n- Tutoring is free.\n- Available subjects: Math, Physics, CS.\n- Next session: May 20, 2026",
        "registration": "Registration:\n- Starts: June 1, 2026\n- Ends: June 15, 2026\n- Add/drop: June 2 – June 6, 2026",
        "counseling": "Counseling:\n- Hours: 8:00 AM – 4:00 PM\n- Days: Mon–Fri\n- Location: Student Affairs Building",
        "attendance_policy": "Attendance Policy:\n- Minimum attendance: 75%\n- Missing class without excuse affects grade",
        "late_submission_policy": "Late Submission:\n- Late work loses 5% per day\n- Extensions require approval",
        "registrar_contact": "Registrar Contact:\n- Email: registrar@university.edu\n- Phone: +234 800 123 4567",
        "support_contact": "Student Support:\n- Email: support@university.edu\n- Office hours: 8:00 AM – 4:00 PM"
    })

    # User input
    user_input = st.text_input("Type your question here:")
    if user_input:
        text = user_input.lower()
        if "exam" in text:
            if any(word in text for word in ["2nd", "second", "sem 2", "semester 2"]):
                intent = "2nd Semester exam"
            elif any(word in text for word in ["1st", "first", "sem 1", "semester 1"]):
                intent = "1st Semester exam"
            else:
                intent = upcoming_semester
        else:
            input_vec = vectorizer.transform([text])
            intent = model.predict(input_vec)[0]

        answer = responses.get(intent, "Sorry, I don't have an answer for that yet.")
        st.write(f"**Bot:** {answer}")
