import constants
import goroda
import copy

cities = copy.deepcopy(goroda.city)

def handle_text(message):
    global cities
    cities = copy.deepcopy(goroda.city)

print("/start" in cities.get("а"))
