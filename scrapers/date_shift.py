from dateutil import parser

def date_handler(date):
    try: 
        date = parser.parse(date)
        date = date.strftime("%a, %b %d, %Y") 
    except Exception as e: 
        print(f"there was an error with {date}, see error {e}")

    return date