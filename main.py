from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Event Notification System is running"}


def job_check_reminders():
    events = get_event_data()
    for event in events:
        # Check if current time matches event time - 24 hours
        # If yes, call Gemini for draft and send_whatsapp()
        pass

scheduler = BackgroundScheduler()
scheduler.add_job(job_check_reminders, 'interval', minutes=30)
scheduler.start()

# # main.py
# from database import get_event_data
# from nlp_engine import process_event_context
# from ai_service import call_gemini

# def run_system():
#     # 1. Get data from Sheet
#     events = get_event_data()
    
#     for event in events:
#         # 2. Use Local AI to find the tone
#         tone = process_event_context(event['Description'])
        
#         # 3. Use Gemini to write the actual message
#         draft = call_gemini(f"Write a {tone} invite for {event['Event Name']}", API_KEY)
        
#         print(f"Ready to send: {draft}")

# if __name__ == "__main__":
#     run_system()