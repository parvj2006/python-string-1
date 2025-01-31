# Loop through 24 hours
for hour in range(24):
    if hour == 0:
        print("12 Midnight")  # 12 AM is midnight
    elif hour == 12:
        print("12 Noon")  # 12 PM is noon
    elif hour < 12:
        print(f"{hour} AM")  # Morning hours (1 AM to 11 AM)
    else:
        print(f"{hour - 12} PM")  # Afternoon and evening hours (1 PM to 11 PM)
