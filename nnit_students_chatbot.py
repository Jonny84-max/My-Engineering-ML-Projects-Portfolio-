import datetime
import streamlit as st
import joblib
from difflib import get_close_matches

# Load model
model = joblib.load("chatbot_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Keyword mapping
keyword_map = {
    "1st Semester exam": ["1st sem", "first semester", "semester 1"],
    "2nd Semester exam": ["2nd sem", "second semester", "semester 2"],
    "assignment and project deadlines": ["assignment", "assignemnt", "project", "deadline"],
    "library": ["library", "books", "hours"],
    "tutoring": ["tutor", "help"],
    "registration": ["register", "registration"],
    "counseling": ["counseling", "support"],
    "attendance_policy": ["attendance"],
    "late_submission_policy": ["late submission"],
    "registrar_contact": ["registrar", "contact"],
    "support_contact": ["support"]
}

def run():
    st.title("📚 Nigerian Navy Institute of Technology: Student Support Chatbot")
    st.write("Ask about exams, assignments, library, registration, etc.")

    # Generate exam schedules
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
        show_days = days_to_start <= 7 if days_to_start > 0 else False

        return first_exam_day, last_exam_day, countdown, show_days, exam_days

    # Generate both semesters
    f_start, f_end, f_count, f_show_days, f_days = get_exam_details(3, 1)
    s_start, s_end, s_count, s_show_days, s_days = get_exam_details(8, 3)

    # YOUR EXACT RESPONSES (verbatim)
    responses = {
        "1st Semester exam": f" First Semester Exam Schedule:\n {f_start.strftime('%d %B %Y')} – {f_end.strftime('%d %B %Y')}\n{f_count}\n{f_days}\n Daily start time: 9:00 AM",
        "2nd Semester exam": f" Second Semester Exam Schedule:\n {s_start.strftime('%d %B %Y')} – {s_end.strftime('%d %B %Y')}\n{s_count}\n{s_days}\n Daily start time: 9:00 AM",
        "assignment and project deadlines": " Assignment and Project Deadlines:\n- Assignment due: May 25, 2026\n- Project due: June 12, 2026",
        "library": " Library Hours:\n- Weekdays: 8:00 AM – 6:00 PM\n- Weekends: 10:00 AM – 4:00 PM",
        "tutoring": " Tutoring:\n- Tutoring is free.\n- Available subjects: Math, Physics, CS.\n- Next session: May 20, 2026",
        "registration": " Registration:\n- Starts: June 1, 2026\n- Ends: June 15, 2026\n- Add/drop: June 2 – June 6, 2026",
        "counseling": " Counseling:\n- Hours: 8:00 AM – 4:00 PM\n- Days: Mon–Fri\n- Location: Student Affairs Building",
        "attendance_policy": " Attendance Policy:\n- Minimum attendance: 75%",
        "late_submission_policy": " Late Submission:\n- Late work loses 5% per day",
        "registrar_contact": " Registrar Contact:\n- Email: registrar@university.edu",
        "support_contact": " Student Support:\n- Email: support@university.edu"
    }

    # Upcoming semester fallback
    upcoming_semester = "1st Semester exam" if datetime.date.today().month <= 6 else "2nd Semester exam"

    # Input
    user_input = st.text_input("Type your question here:")

    if user_input:
        text = user_input.lower()
        matched_intent = None

        # Keyword matching
        for intent_key, keywords in keyword_map.items():
            for kw in keywords:
                if kw in text or get_close_matches(text, [kw], cutoff=0.8):
                    matched_intent = intent_key
                    break
            if matched_intent:
                break

        # Generic exam fallback
        if not matched_intent and "exam" in text:
            matched_intent = upcoming_semester

        # ML fallback
        if not matched_intent:
            input_vec = vectorizer.transform([text])
            matched_intent = model.predict(input_vec)[0]

        # Final response
        answer = responses.get(
            matched_intent,
            "Hmm, I’m not sure about that yet 🤔. I can help with exams, assignments, library info, registration, or tutoring."
        )

        st.write(f"**Bot:** {answer}")

# IMPORTANT for portfolio
if __name__ == "__main__":
    run()
