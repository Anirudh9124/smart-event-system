from twilio.rest import Client

def send_whatsapp(to_number, message_body):
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    client.messages.create(
        from_='whatsapp:+14155238886', # Twilio Sandbox Number
        body=message_body,
        to=f'whatsapp:{+919346709124}'
    )