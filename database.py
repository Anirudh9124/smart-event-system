import gspread
from oauth2client.service_account import ServiceAccountCredentials
def get_event_data():
    scope = ["[https://spreadsheets.google.com/feeds](https://spreadsheets.google.com/feeds)", "[https://www.googleapis.com/auth/drive](https://www.googleapis.com/auth/drive)"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Your Sheet Name").sheet1
    return sheet.get_all_records()