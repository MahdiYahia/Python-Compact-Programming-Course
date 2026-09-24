def sort_by_colors_alphabetical_order(items):
    return sorted(items, key=lambda item: item["color"])


if __name__ == "__main__":
    phones = [
        {"make": " Google ", "model": 216, "color": "Black"},
        {"make": "Mi Max", "model": 2, "color": "Gold"},
        {"make": "Samsung", "model": 7, "color": "Blue"},
    ]
    print(sort_by_colors_alphabetical_order(phones))