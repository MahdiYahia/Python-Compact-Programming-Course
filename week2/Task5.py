events = {
    "Warm Up mit Dennis Streichert und Maxim Diagilew": "19.09.2026",
    "Marquess": "19.09.2026",
    "Musikfeuerwerk": "19.09.2026",
    "Vom Stein zum Stahl": "20.09.2026",
    "Stahlzeit in Dortmund": "20.09.2026",
    "Dortmund – Stadt des Bieres": "20.09.2026"
}

selected_date = "19.09.2026"

for event, event_date in events.items():
    if event_date == selected_date:
        print(event)