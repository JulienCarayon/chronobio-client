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
    LAYOFF_DAY,
    TRACTOR_BUSY_DAY_FROM_FACTORY,
)

game_data = {
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
    aigrisculteurs.get_my_farm()

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
    aigrisculteurs.get_my_farm()

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
    aigrisculteurs.get_my_farm()

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
    aigrisculteurs.get_my_farm()

    aigrisculteurs.hiring_workers(10)
    aigrisculteurs.worker_daily_task_new_day()
    assert (aigrisculteurs.worker_daily_task["worker1"]) == "None"


def test_get_my_farm(aigrisculteurs):

    raisedError = None

    try:
        aigrisculteurs.get_my_farm()
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
        aigrisculteurs.get_my_farm()
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
        aigrisculteurs.get_my_farm()
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
    aigrisculteurs.get_my_farm()

    aigrisculteurs.hiring_workers(1)
    assert aigrisculteurs.check_worker_availability(1) == True

    aigrisculteurs.worker_sow_vegetable_at_field(1, TOMATO[1], 1)
    assert aigrisculteurs.check_worker_availability(1) == False


def test_send_worker_to_place(aigrisculteurs):

    game = {
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
                        "content": "TOMATO",
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
    aigrisculteurs.game_data = game
    aigrisculteurs.get_my_farm()
    aigrisculteurs.day = 0

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

    aigrisculteurs.game_data = game_data
    aigrisculteurs.get_my_farm()

    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.send_worker_to_place(worker_id=4, place=2)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "4 SEMER PATATE 2"

    aigrisculteurs.send_worker_to_place(worker_id=1, place=FACTORY_SOUPE)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "4 SEMER PATATE 2"

    aigrisculteurs.send_worker_to_place(worker_id=1, place=FACTORY_SOUPE)

    aigrisculteurs.game_data = game
    aigrisculteurs.get_my_farm()

    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.buy_tractors(1)
    aigrisculteurs.my_farm["tractors"] = [{"location": "FARM", "id": 1}]

    aigrisculteurs.send_worker_to_place(
        worker_id=5, place=FACTORY_STOCK, tractor_id=1, field_to_collect=4
    )
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "5 STOCKER 4 1"

    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.buy_tractors(3)
    aigrisculteurs.my_farm["tractors"] = [
        {"location": "FARM", "id": 1},
        {"location": "FARM", "id": 2},
        {"location": "FARM", "id": 3},
        {"location": "FARM", "id": 4},
    ]

    aigrisculteurs.send_worker_to_place(
        worker_id=659, place=FACTORY_STOCK, tractor_id=2, field_to_collect=1
    )
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "0 ACHETER_TRACTEUR"

    # aigrisculteurs.game_data = game
    # aigrisculteurs.new_day()
    aigrisculteurs.my_farm[FIELDS][3][
        "content"
    ] = "LEEK"  # erasing myfarm data with game_data
    aigrisculteurs.worker_daily_task[f"worker5"] = "None"
    logging.debug(f"Worker 4 : {aigrisculteurs.check_worker_availability(4)}")
    logging.debug(f"Worker 5 : {aigrisculteurs.check_worker_availability(5)}")
    logging.debug(f"Is field 4 sown : {aigrisculteurs.check_if_field_sown(4)}")
    logging.debug(
        f' Is field 4 sown (again) {aigrisculteurs.my_farm[FIELDS][4 - 1].get("content")}'
    )
    logging.debug(
        f"Does field 4 need water: {aigrisculteurs.check_if_field_need_water(4)}"
    )
    logging.debug(
        f"Is field 4 bought : {aigrisculteurs.my_farm[FIELDS][4-1].get('bought')}"
    )
    logging.debug(
        f"Is field 4 collectable : {aigrisculteurs.check_if_field_collectable(4)}"
    )
    aigrisculteurs.send_worker_to_place(tractor_id=1, field_to_collect=4)
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
    aigrisculteurs.get_my_farm()

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
    aigrisculteurs.get_my_farm()
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
    aigrisculteurs.get_my_farm()
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
    aigrisculteurs.get_my_farm()
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
    aigrisculteurs.get_my_farm()
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
    aigrisculteurs.get_my_farm()
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
    aigrisculteurs.get_my_farm()
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
    aigrisculteurs.get_my_farm()
    aigrisculteurs.hiring_workers(1)
    logging.debug(
        f"NUMBER OF EMPLOYEE {aigrisculteurs.actual_number_of_workers}")

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
    aigrisculteurs.get_my_farm()

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

    aigrisculteurs.get_my_farm()
    assert aigrisculteurs.check_if_field_collectable(1) == False
    assert aigrisculteurs.check_if_field_collectable(2) == False
    assert aigrisculteurs.check_if_field_collectable(3) == False
    assert aigrisculteurs.check_if_field_collectable(4) == True


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
    aigrisculteurs.get_my_farm()
    aigrisculteurs.hiring_workers(4)
    aigrisculteurs.buy_tractors(5)
    aigrisculteurs.my_farm["tractors"] = [
        {"location": "FARM", "id": 1},
        {"location": "FARM", "id": 2},
        {"location": "FARM", "id": 3},
        {"location": "FARM", "id": 4},
        {"location": "FARM", "id": 5},
    ]

    aigrisculteurs.store_with_tractor(worker_id=1, tractor_id=1, field_id=4)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 STOCKER 4 1"

    aigrisculteurs.store_with_tractor(worker_id=2, tractor_id=80, field_id=2)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 STOCKER 4 1"

    aigrisculteurs.store_with_tractor(worker_id=1, tractor_id=1, field_id=2)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 STOCKER 4 1"

    aigrisculteurs.store_with_tractor(worker_id=3, tractor_id=1, field_id=3)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 STOCKER 4 1"

    aigrisculteurs.store_with_tractor(worker_id=4, tractor_id=3, field_id=4)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 STOCKER 4 1"


def test_new_day(aigrisculteurs):
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
    aigrisculteurs.get_my_farm()
    aigrisculteurs.hiring_workers(3)
    aigrisculteurs.send_worker_to_place(worker_id=1, place=1)
    assert aigrisculteurs.check_worker_availability(1) == False
    aigrisculteurs.new_day()
    assert aigrisculteurs.check_worker_availability(1) == True


def test_send_group_to_place(aigrisculteurs):
    aigrisculteurs.game_data = game_data
    aigrisculteurs.get_my_farm()
    aigrisculteurs.aigrisculteurs_commands.clear()
    aigrisculteurs.buy_fields(5)
    aigrisculteurs.hiring_workers(3)
    aigrisculteurs.send_group_to_place(1, 2, 1)
    logging.debug(
        f"PREVIOUS ACTIONS :  {aigrisculteurs.aigrisculteurs_commands}")
    logging.debug(f"FIELD 1 SOWN ? {aigrisculteurs.check_if_field_sown(1)}")
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "2 ARROSER 1"


# def test_run_not_crashing(aigrisculteurs):
#     aigrisculteurs.game_data = game_data
#     aigrisculteurs.get_my_farm()
#     for day in range(0, 1800):
#         logging.info(f"--DAY {day}--")
#         aigrisculteurs.day = day
#         assert (
#             aigrisculteurs.run(
#                 aigrisculteurs.game_data, testing=True, should_crash=False
#             )
#             == "Day went successfully"
#         )


# def test_run_crashing(aigrisculteurs):
#     aigrisculteurs.game_data = game_data
#     aigrisculteurs.get_my_farm()
#     for day in range(0, 1800):
#         logging.info(f"--DAY {day}--")
#         aigrisculteurs.day = day
#         assert (
#             aigrisculteurs.run(
#                 aigrisculteurs.game_data, testing=True, should_crash=True
#             )
#             == "Day crashed"
#         )


def test_set_number_of_busy_day_for_tractor(aigrisculteurs):
    aigrisculteurs.game_data = game_data
    aigrisculteurs.get_my_farm()

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

    tractor_id, field_id = 3, 5
    aigrisculteurs.set_number_of_busy_day_for_tractor(tractor_id, field_id)
    assert (aigrisculteurs.tractor_data[tractor_id - 1][N_BUSY_DAY]) == 1
    # == TRACTOR_BUSY_DAY_FROM_FACTORY[f"FIELD{field_id}"]


def test_update_number_of_busy_day_for_tractor(aigrisculteurs):
    aigrisculteurs.game_data = game_data
    aigrisculteurs.get_my_farm()
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


def test_update_local_day(aigrisculteurs):
    aigrisculteurs.day = 0
    aigrisculteurs.update_local_day()
    assert (aigrisculteurs.local_day) == 0

    aigrisculteurs.day = 1
    for _ in range(56):
        aigrisculteurs.update_local_day()
        aigrisculteurs.day += 1
    assert (aigrisculteurs.local_day) == 56

    aigrisculteurs.day = 1
    for _ in range(450):
        aigrisculteurs.update_local_day()
        aigrisculteurs.day += 1
    assert (aigrisculteurs.local_day) == 0


def test_fire_workers(aigrisculteurs):
    aigrisculteurs.game_data = game_data
    aigrisculteurs.get_my_farm()

    aigrisculteurs.hiring_workers(12)
    aigrisculteurs.buy_fields(1)
    aigrisculteurs.buy_tractors(1)
    for id in range(1, 12):
        aigrisculteurs.send_worker_to_place(worker_id=id, place=1)
    aigrisculteurs.send_worker_to_place(
        worker_id=12, tractor_id=1, field_to_collect=1)
    aigrisculteurs.fire_workers()
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "0 LICENCIER 11"


def test_sell_field(aigrisculteurs):
    raisedError = None
    try:
        aigrisculteurs.sell_field(field_id=8)
    except Exception as ex:
        raisedError = True
        logging.debug(f"{ex} exception raised")
    else:
        raisedError = False
        logging.debug("TypeError exception not raised")
    assert raisedError == True

    aigrisculteurs.sell_field(field_id=3)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "0 VENDRE 3"

    aigrisculteurs.sell_field(field_id=1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "0 VENDRE 1"


def test_go_to_cook(aigrisculteurs):
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
    aigrisculteurs.get_my_farm()
    aigrisculteurs.go_to_cook()
    assert (aigrisculteurs.flag_help_cooker) == False

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
                        "POTATO": 55_000,
                        "LEEK": 55_000,
                        "TOMATO": 55_000,
                        "ONION": 55_000,
                        "ZUCCHINI": 55_000,
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
    aigrisculteurs.get_my_farm()
    aigrisculteurs.go_to_cook()
    assert (aigrisculteurs.flag_help_cooker) == True
