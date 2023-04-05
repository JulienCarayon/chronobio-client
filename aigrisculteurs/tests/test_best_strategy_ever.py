from src.best_strategy_ever import Aigrisculteurs
import logging
import pytest

# import json
from src.constants import (
    MAXIMUM_FIELDS_NUMBER,
    WORKERS,
    LOCATION,
    FIELDS,
    NEEDED_WATER,
    STOCK,
    FACTORY_SOUPE,
    FACTORY_STOCK,
    POTATO,
    LEEK,
    TOMATO,
    ONION,
    ZUCCHINI,
    VEGETABLES,
    N_BUSY_DAY,
    TRACTOR_BUSY_DAY_FROM_FACTORY,
)

logging.basicConfig(
    filename="tests.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)-8s] %(filename)20s(%(lineno)3s):%(funcName)-20s :: %(message)s",  # noqa: E501
    datefmt="%m/%d/%Y %H:%M:%S",
)


@pytest.fixture
def aigrisculteurs():
    return Aigrisculteurs()


def verify_answer(expected, answer):
    assert expected == answer


def test_hiring_workers(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()

    aigrisculteurs.hiring_workers(10)
    assert (aigrisculteurs.actual_number_of_workers) == 10
    aigrisculteurs.hiring_workers(90)
    assert (aigrisculteurs.actual_number_of_workers) == 100
    assert (aigrisculteurs.worker_daily_task["worker100"]) == "None"


def test_buy_fields(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()

    aigrisculteurs.buy_fields(2)
    assert (aigrisculteurs.number_of_fields) == 2
    aigrisculteurs.buy_fields(1)
    assert (aigrisculteurs.number_of_fields) == 3
    aigrisculteurs.buy_fields(600)
    assert (aigrisculteurs.number_of_fields) == 5


def test_buy_tractors(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()

    aigrisculteurs.buy_tractors(10)
    assert (aigrisculteurs.actual_number_of_tractors) == 10
    aigrisculteurs.buy_tractors(3)
    assert (aigrisculteurs.actual_number_of_tractors) == 13
    aigrisculteurs.buy_tractors(1)
    assert (aigrisculteurs.actual_number_of_tractors) == 14
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "0 ACHETER_TRACTEUR"


def test_add_command(aigrisculteurs):
    aigrisculteurs.add_command("0 ACHETER_TRACTEUR")
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "0 ACHETER_TRACTEUR"


def test_do_bank_loan(aigrisculteurs):
    aigrisculteurs.do_bank_loan(5500)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "0 EMPRUNTER 5500"


def test_worker_daily_task_new_day(aigrisculteurs):
    aigrisculteurs.hiring_workers(10)
    aigrisculteurs.worker_daily_task_new_day()
    assert (aigrisculteurs.worker_daily_task["worker1"]) == "None"


def test_get_my_farm_json(aigrisculteurs):

    raisedError = None

    try:
        aigrisculteurs.get_my_farm_json()
    except Exception as ex:
        raisedError = True
        logging.debug(f"{ex} exception raised")
    else:
        raisedError = False
        logging.debug("TypeError exception not raised")

    assert raisedError == True

    raisedError = None
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "hello",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "aigrisculteurs",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }

    try:
        aigrisculteurs.get_my_farm_json()
    except Exception as ex:
        raisedError = True
        logging.debug(f"{ex} exception raised")
    else:
        raisedError = False
        logging.debug("TypeError exception not raised")

    assert raisedError == False

    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "hello",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "none",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }

    raisedError = None

    try:
        aigrisculteurs.get_my_farm_json()
    except Exception as ex:
        raisedError = True
        logging.debug(f"{ex} exception raised")
    else:
        raisedError = False
        logging.debug("TypeError exception not raised")

    assert raisedError == True
    aigrisculteurs.hiring_workers(10)


def test_check_worker_availability(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()

    aigrisculteurs.hiring_workers(1)
    assert aigrisculteurs.check_worker_availability(1) == True

    aigrisculteurs.worker_sow_vegetable_at_field(1, TOMATO[1], 1)
    assert aigrisculteurs.check_worker_availability(1) == False


def test_send_worker_to_place(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "POTATO",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()

    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.send_worker_to_place(worker_id=1, place=FACTORY_SOUPE)
    # logging.debug(f"IS WORKER AVAILABLE : {aigrisculteurs.check_worker_availability(1) }")

    aigrisculteurs.send_worker_to_place(worker_id=1, place=1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 CUISINER"

    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.send_worker_to_place(worker_id=2, place=6)
    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.send_worker_to_place(worker_id=3, place=1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "3 ARROSER 1"

    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "POTATO",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()

    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.send_worker_to_place(worker_id=4, place=2)
    logging.debug(f"GAME_DATA: {aigrisculteurs.game_data}")
    logging.debug(f"FIELD 1 SOWN ? : {aigrisculteurs.check_if_field_sown(1)}")
    logging.debug(f"FIELD 2 SOWN ? : {aigrisculteurs.check_if_field_sown(2)}")
    logging.debug(f"FIELD 3 SOWN ? : {aigrisculteurs.check_if_field_sown(3)}")
    logging.debug(f"FIELD 4 SOWN ? : {aigrisculteurs.check_if_field_sown(4)}")
    logging.debug(f"FIELD 5 SOWN ? : {aigrisculteurs.check_if_field_sown(5)}")
    logging.debug(
        f"FIELD 2 NEED WATER ? : {aigrisculteurs.check_if_field_need_water(2)}"
    )
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "4 SEMER POIREAU 2"

    aigrisculteurs.send_worker_to_place(worker_id=1, place=FACTORY_SOUPE)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "4 SEMER POIREAU 2"

    aigrisculteurs.send_worker_to_place(worker_id=1, place=FACTORY_SOUPE)

    aigrisculteurs.send_worker_to_place(1, FACTORY_SOUPE)

    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "TOMATO",
                        "needed_water": 4,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 2,
                        "bought": True,
                        "location": "FIELD3",
                    },
                    {
                        "content": "POTATO",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()

    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.buy_tractors(1)
    aigrisculteurs.send_worker_to_place(
        worker_id=5, place=FACTORY_STOCK, tractor_id=1, field_to_collect=4
    )
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "5 STOCKER 4 1"

    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.buy_tractors(1)
    aigrisculteurs.send_worker_to_place(
        worker_id=6, place=FACTORY_STOCK, tractor_id=2, field_to_collect=1
    )
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "0 ACHETER_TRACTEUR"
    # logging.debug(f"IS WORKER AVAILABLE : {aigrisculteurs.check_worker_availability(1) }")


def test_get_vegetables_stock(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()

    logging.debug(aigrisculteurs.get_vegetables_stock())
    assert (aigrisculteurs.get_vegetables_stock()) == {
        "POTATO": 0,
        "LEEK": 0,
        "TOMATO": 0,
        "ONION": 0,
        "ZUCCHINI": 0,
    }

    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()
    assert (aigrisculteurs.get_vegetables_stock()) == {
        "POTATO": 1,
        "LEEK": 2,
        "TOMATO": 3,
        "ONION": 4,
        "ZUCCHINI": 5,
    }


def test_check_if_field_sown(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }

    raisedError = None

    try:
        aigrisculteurs.check_if_field_sown(-1)

    except Exception as ex:
        raisedError = True
        logging.debug(f"{ex} exception raised")
    else:
        raisedError = False
        logging.debug("TypeError exception not raised")

    assert raisedError == True

    raisedError = None

    try:
        aigrisculteurs.check_if_field_sown(6)

    except Exception as ex:
        raisedError = True
        logging.debug(f"{ex} exception raised")
    else:
        raisedError = False
        logging.debug("TypeError exception not raised")

    assert raisedError == True

    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()
    assert aigrisculteurs.check_if_field_sown(1) == False

    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "TOMATO",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()
    assert aigrisculteurs.check_if_field_sown(1) == False

    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "TOMATO",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()
    assert aigrisculteurs.check_if_field_sown(1) == True


def test_worker_sow_vegetable_at_field(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()
    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.worker_sow_vegetable_at_field(1, TOMATO[1], 1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 SEMER TOMATE 1"

    aigrisculteurs.worker_sow_vegetable_at_field(1, LEEK[1], 1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 SEMER TOMATE 1"

    aigrisculteurs.hiring_workers(2)
    aigrisculteurs.worker_sow_vegetable_at_field(2, "CITROUILLE", 1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "0 EMPLOYER"


def test_less_stocked_vegetable(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()
    logging.debug(
        f"Less stocked vegetables {aigrisculteurs.get_less_stocked_vegetable()}"
    )
    assert aigrisculteurs.get_less_stocked_vegetable() == "PATATE"


def test_seed_less_stocked_vegetable(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()
    aigrisculteurs.hiring_workers(1)
    logging.debug(f"NUMBER OF EMPLOYEE {aigrisculteurs.actual_number_of_workers}")

    aigrisculteurs.seed_less_stocked_vegetable(1, 1)
    assert aigrisculteurs.aigrisculteurs_commands[-1] == "1 SEMER PATATE 1"


def test_check_if_field_need_water(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "POTATO",
                        "needed_water": 1,
                        "bought": True,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()

    raisedError = None

    try:
        aigrisculteurs.check_if_field_need_water(7)

    except Exception as ex:
        raisedError = True
        logging.debug(f"{ex} exception raised")
    else:
        raisedError = False
        logging.debug("ValueError exception not raised")

    assert raisedError == True

    raisedError = None

    assert aigrisculteurs.check_if_field_need_water(1) == False
    assert aigrisculteurs.check_if_field_need_water(2) == True
    assert aigrisculteurs.check_if_field_need_water(3) == False


def test_check_if_field_collectable(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "TOMATO",
                        "needed_water": 4,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 2,
                        "bought": True,
                        "location": "FIELD3",
                    },
                    {
                        "content": "POTATO",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }

    aigrisculteurs.get_my_farm_json()
    assert aigrisculteurs.check_if_field_collectable(1) == False
    assert aigrisculteurs.check_if_field_collectable(2) == False
    assert aigrisculteurs.check_if_field_collectable(3) == False
    assert aigrisculteurs.check_if_field_collectable(4) == True


def test_run(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    for day in range(0, 1800):
        aigrisculteurs.get_my_farm_json()
        aigrisculteurs.game_data = {
            "day": day,
            "greenhouse_gas": 0,
            "events": [],
            "farms": [
                {
                    "blocked": False,
                    "name": "aigrisculteurs",
                    "money": 100030,
                    "score": 100030,
                    "fields": [
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD1",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD2",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD3",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD4",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD5",
                        },
                    ],
                    "tractors": [],
                    "loans": [],
                    "soup_factory": {
                        "days_off": 0,
                        "stock": {
                            "POTATO": 1,
                            "LEEK": 2,
                            "TOMATO": 3,
                            "ONION": 4,
                            "ZUCCHINI": 5,
                        },
                    },
                    "employees": [],
                    "events": [],
                },
                {
                    "blocked": True,
                    "name": "",
                    "money": 100000,
                    "score": 100000,
                    "fields": [
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD1",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD2",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD3",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD4",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD5",
                        },
                    ],
                    "tractors": [],
                    "loans": [],
                    "soup_factory": {
                        "days_off": 0,
                        "stock": {
                            "POTATO": 0,
                            "LEEK": 0,
                            "TOMATO": 0,
                            "ONION": 0,
                            "ZUCCHINI": 0,
                        },
                    },
                    "employees": [],
                    "events": [],
                },
                {
                    "blocked": True,
                    "name": "",
                    "money": 100000,
                    "score": 100000,
                    "fields": [
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD1",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD2",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD3",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD4",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD5",
                        },
                    ],
                    "tractors": [],
                    "loans": [],
                    "soup_factory": {
                        "days_off": 0,
                        "stock": {
                            "POTATO": 0,
                            "LEEK": 0,
                            "TOMATO": 0,
                            "ONION": 0,
                            "ZUCCHINI": 0,
                        },
                    },
                    "employees": [],
                    "events": [],
                },
                {
                    "blocked": True,
                    "name": "",
                    "money": 100000,
                    "score": 100000,
                    "fields": [
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD1",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD2",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD3",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD4",
                        },
                        {
                            "content": "NONE",
                            "needed_water": 0,
                            "bought": False,
                            "location": "FIELD5",
                        },
                    ],
                    "tractors": [],
                    "loans": [],
                    "soup_factory": {
                        "days_off": 0,
                        "stock": {
                            "POTATO": 0,
                            "LEEK": 0,
                            "TOMATO": 0,
                            "ONION": 0,
                            "ZUCCHINI": 0,
                        },
                    },
                    "employees": [],
                    "events": [],
                },
            ],
        }

        assert (
            aigrisculteurs.run(aigrisculteurs.game_data, testing=False)
            == "Day went successfully"
        )
        assert (
            aigrisculteurs.run(aigrisculteurs.game_data, testing=True) == "Day crashed"
        )


def test_store_with_tractor(aigrisculteurs):
    aigrisculteurs.game_data = {
        "day": 0,
        "greenhouse_gas": 0,
        "events": [],
        "farms": [
            {
                "blocked": False,
                "name": "aigrisculteurs",
                "money": 100030,
                "score": 100030,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "TOMATO",
                        "needed_water": 4,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "LEEK",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD3",
                    },
                    {
                        "content": "POTATO",
                        "needed_water": 0,
                        "bought": True,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 1,
                        "LEEK": 2,
                        "TOMATO": 3,
                        "ONION": 4,
                        "ZUCCHINI": 5,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
            {
                "blocked": True,
                "name": "",
                "money": 100000,
                "score": 100000,
                "fields": [
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD1",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD2",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD3",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD4",
                    },
                    {
                        "content": "NONE",
                        "needed_water": 0,
                        "bought": False,
                        "location": "FIELD5",
                    },
                ],
                "tractors": [],
                "loans": [],
                "soup_factory": {
                    "days_off": 0,
                    "stock": {
                        "POTATO": 0,
                        "LEEK": 0,
                        "TOMATO": 0,
                        "ONION": 0,
                        "ZUCCHINI": 0,
                    },
                },
                "employees": [],
                "events": [],
            },
        ],
    }
    aigrisculteurs.get_my_farm_json()
    aigrisculteurs.hiring_workers(3)
    aigrisculteurs.buy_tractors(5)
    aigrisculteurs.store_with_tractor(worker_id=1, tractor_id=1, field_id=4)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 STOCKER 4 1"

    aigrisculteurs.store_with_tractor(worker_id=2, tractor_id=80, field_id=2)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 STOCKER 4 1"

    aigrisculteurs.store_with_tractor(worker_id=1, tractor_id=1, field_id=2)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 STOCKER 4 1"

    aigrisculteurs.store_with_tractor(worker_id=3, tractor_id=1, field_id=3)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 STOCKER 4 1"


def test_set_number_of_busy_day_for_tractor(aigrisculteurs):
    aigrisculteurs.buy_tractors(5)

    raisedError = None
    try:
        tractor_id, field_id = 7, 2
        aigrisculteurs.set_number_of_busy_day_for_tractor(tractor_id, field_id)
    except Exception as ex:
        raisedError = True
        logging.debug(f"{ex} exception raised")
    else:
        raisedError = False
        logging.debug("TypeError exception not raised")
    assert raisedError == True

    raisedError = None
    try:
        tractor_id, field_id = 3, 8
        aigrisculteurs.set_number_of_busy_day_for_tractor(tractor_id, field_id)
    except Exception as ex:
        raisedError = True
        logging.debug(f"{ex} exception raised")
    else:
        raisedError = False
        logging.debug("TypeError exception not raised")
    assert raisedError == True

    tractor_id, field_id = 1, 2
    aigrisculteurs.set_number_of_busy_day_for_tractor(tractor_id, field_id)
    assert (aigrisculteurs.tractor_data[tractor_id - 1][N_BUSY_DAY]) == 3
    # == TRACTOR_BUSY_DAY_FROM_FACTORY[f"FIELD{field_id}"]

    tractor_id, field_id = 3, 4
    aigrisculteurs.set_number_of_busy_day_for_tractor(tractor_id, field_id)
    assert (aigrisculteurs.tractor_data[tractor_id - 1][N_BUSY_DAY]) == 1
    # == TRACTOR_BUSY_DAY_FROM_FACTORY[f"FIELD{field_id}"]


def test_update_number_of_busy_day_for_tractor(aigrisculteurs):
    aigrisculteurs.buy_tractors(5)
    tractor_id, field_id = 1, 3
    aigrisculteurs.set_number_of_busy_day_for_tractor(tractor_id, field_id)
    aigrisculteurs.update_number_of_busy_day_for_tractor()
    assert (aigrisculteurs.tractor_data[tractor_id - 1][N_BUSY_DAY]) == 0

    tractor_id, field_id = 4, 1
    aigrisculteurs.set_number_of_busy_day_for_tractor(tractor_id, field_id)
    aigrisculteurs.update_number_of_busy_day_for_tractor()
    assert (aigrisculteurs.tractor_data[tractor_id - 1][N_BUSY_DAY]) == 2
    aigrisculteurs.update_number_of_busy_day_for_tractor()
    assert (aigrisculteurs.tractor_data[tractor_id - 1][N_BUSY_DAY]) == 1
    aigrisculteurs.update_number_of_busy_day_for_tractor()
    assert (aigrisculteurs.tractor_data[tractor_id - 1][N_BUSY_DAY]) == 0
    aigrisculteurs.update_number_of_busy_day_for_tractor()
    assert (aigrisculteurs.tractor_data[tractor_id - 1][N_BUSY_DAY]) == 0
