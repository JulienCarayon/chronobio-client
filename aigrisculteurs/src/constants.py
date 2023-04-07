MAXIMUM_FIELDS_NUMBER = 5
WORKERS = "employees"
WORKER = "worker"
DAY = "day"

LOCATION = "location"
DESTINATION = "destination"
FIELDS = "fields"
FARM = "FARM"

LAYOFF_DAY = 450
NUMBER_OF_COOKER = 8

LOAN_AMOUNT = 69_970

STOCK = "stock"
NEEDED_WATER = "needed_water"
FACTORY_SOUPE = ("soup_factory", "CUISINER", "SOUP_FACTORY")
FACTORY_STOCK = ("USINE", "SOUP_FACTORY")
CONTENT = "content"
TRACTORS = "tractors"
N_BUSY_DAY = "n_busy_day"

POTATO = ("POTATO", "PATATE")
LEEK = ("LEEK", "POIREAU")
TOMATO = ("TOMATO", "TOMATE")
ONION = ("ONION", "OIGNON")
ZUCCHINI = ("ZUCCHINI", "COURGETTE")

VEGETABLES = {
    "POTATO": "PATATE",
    "LEEK": "POIREAU",
    "TOMATO": "TOMATE",
    "ONION": "OIGNON",
    "ZUCCHINI": "COURGETTE",
}

TRACTOR_BUSY_DAY_FROM_FACTORY = {
    "FIELD1": 3,
    "FIELD2": 3,
    "FIELD3": 1,
    "FIELD4": 1,
    "FIELD5": 1,
}

WORKER_ID_INDEX = {
    0: [1, 12, 23, 38],  # [group1, group2, group3, cooker]
    1: [46, 57, 68, 79],
    2: [87, 98, 109, 120],
    3: [128, 139, 150, 161],
    4: [169, 180, 191, 202],
    5: [210, 221, 232, 243],
    6: [251, 262, 273, 284],
    7: [292, 303, 314, 325],
    8: [333, 344, 355, 366],
    9: [374, 385, 396, 407],
    10: [415, 426, 437, 448],
    11: [456, 467, 478, 489],
    12: [497, 508, 519, 530],
    13: [538, 549, 560, 571],
    14: [579, 590, 601, 612],
    15: [620, 631, 642, 653],
}
