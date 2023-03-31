from src.best_startegy_ever import Aigrisculteurs
import logging
import pytest
import json
from src.constants import (
                            MAXIMUM_FIELDS_NUMBER,
                            WORKERS,
                            LOCATION,
                            FIELDS,
                            NEEDED_WATER,
                            FACTORY,
                            STOCK,
                            POTATO,
                            LEEK,
                            TOMATO,
                            ONION,
                            ZUCCHINI)

logging.basicConfig(
    filename="tests.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)-8s] %(filename)20s(%(lineno)3s):%(funcName)-20s :: %(message)s",  # noqa: E501
    datefmt="%m/%d/%Y %H:%M:%S"
)



@pytest.fixture
def aigrisculteurs():
    return Aigrisculteurs()


def verify_answer(expected, answer):
    assert expected == answer


def test_hiring_workers(aigrisculteurs):
    aigrisculteurs.hiring_workers(10)
    assert (aigrisculteurs.actual_number_of_workers) == 10
    aigrisculteurs.hiring_workers(90)
    assert (aigrisculteurs.actual_number_of_workers) == 100
    assert (aigrisculteurs.worker_daily_task["worker100"]) == "None"


def test_hiring_workers(aigrisculteurs):
    aigrisculteurs.hiring_workers(10)
    assert (aigrisculteurs.actual_number_of_workers) == 10
    aigrisculteurs.hiring_workers(90)
    assert (aigrisculteurs.actual_number_of_workers) == 100
    assert (aigrisculteurs.worker_daily_task["worker100"]) == "None"


def test_buy_fields(aigrisculteurs):
    aigrisculteurs.buy_fields(2)
    assert (aigrisculteurs.number_of_fields) == 2
    aigrisculteurs.buy_fields(1)
    assert (aigrisculteurs.number_of_fields) == 3
    aigrisculteurs.buy_fields(600)
    assert (aigrisculteurs.number_of_fields) == 5


def test_buy_tractors(aigrisculteurs):
    aigrisculteurs.buy_tactors(10)
    assert (aigrisculteurs.actual_number_of_tractors) == 10
    aigrisculteurs.buy_tactors(3)
    assert (aigrisculteurs.actual_number_of_tractors) == 13
    aigrisculteurs.buy_tactors(1)
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
        logging.debug(f'{ex} exception raised')
    else:
        raisedError = False
        logging.debug('TypeError exception not raised')

    assert(raisedError == True)

    raisedError = None
    aigrisculteurs.game_data = {'day': 0, 'greenhouse_gas': 0, 'events': [], 'farms': [{'blocked': False, 'name': 'hello', 'money': 100030, 'score': 100030, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': 'aigrisculteurs', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}]}
    
    try:
        aigrisculteurs.get_my_farm_json()
    except Exception as ex:
        raisedError = True
        logging.debug(f'{ex} exception raised')
    else:
        raisedError = False
        logging.debug('TypeError exception not raised')


    assert(raisedError == False)
    

    aigrisculteurs.game_data = {'day': 0, 'greenhouse_gas': 0, 'events': [], 'farms': [{'blocked': False, 'name': 'hello', 'money': 100030, 'score': 100030, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': 'none', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}]}
    
    raisedError = None
   
    try:
        aigrisculteurs.get_my_farm_json()
    except Exception as ex:
        raisedError = True
        logging.debug(f'{ex} exception raised')
    else:
        raisedError = False
        logging.debug('TypeError exception not raised')

    assert(raisedError == True)
    aigrisculteurs.hiring_workers(10)

def test_check_worker_availability(aigrisculteurs):
    aigrisculteurs.hiring_workers(1)
    assert (aigrisculteurs.check_worker_availability(1) == True)
    
    aigrisculteurs.worker_sow_vegetable_at_field(1, TOMATO[1],1)
    assert (aigrisculteurs.check_worker_availability(1) == False)


def test_send_worker_to_place(aigrisculteurs):
    aigrisculteurs.game_data = {'day': 0, 'greenhouse_gas': 0, 'events': [], 'farms': [{'blocked': False, 'name': 'aigrisculteurs', 'money': 100030, 'score': 100030, 'fields': [{'content': 'POTATO', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 1, 'LEEK': 2, 'TOMATO': 3, 'ONION': 4, 'ZUCCHINI': 5}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}]}
    aigrisculteurs.get_my_farm_json()


    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.send_worker_to_place(1,FACTORY)
    logging.debug(f"IS WORKER AVAILABLE : {aigrisculteurs.check_worker_availability(1) }")
    
    aigrisculteurs.send_worker_to_place(1,1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 CUISINER"

    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.send_worker_to_place(2,6)
    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.send_worker_to_place(3,1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "3 ARROSER 1"
    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.send_worker_to_place(4,2)
    
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "4 SEMER PATATE 2"
    aigrisculteurs.send_worker_to_place(1,FACTORY)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "4 SEMER PATATE 2"
    logging.debug(f"IS WORKER AVAILABLE : {aigrisculteurs.check_worker_availability(1) }")


def test_get_vegetables_stock(aigrisculteurs):
    aigrisculteurs.game_data = {'day': 0, 'greenhouse_gas': 0, 'events': [], 'farms': [{'blocked': False, 'name': 'aigrisculteurs', 'money': 100030, 'score': 100030, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}]}
    aigrisculteurs.get_my_farm_json()

    logging.debug(aigrisculteurs.get_vegetables_stock())
    assert (aigrisculteurs.get_vegetables_stock()) == {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}

    aigrisculteurs.game_data = {'day': 0, 'greenhouse_gas': 0, 'events': [], 'farms': [{'blocked': False, 'name': 'aigrisculteurs', 'money': 100030, 'score': 100030, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 1, 'LEEK': 2, 'TOMATO': 3, 'ONION': 4, 'ZUCCHINI': 5}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}]}
    aigrisculteurs.get_my_farm_json()
    assert (aigrisculteurs.get_vegetables_stock()) == {'POTATO': 1, 'LEEK': 2, 'TOMATO': 3, 'ONION': 4, 'ZUCCHINI': 5}

def test_check_if_field_sown(aigrisculteurs):
    aigrisculteurs.game_data = {'day': 0, 'greenhouse_gas': 0, 'events': [], 'farms': [{'blocked': False, 'name': 'aigrisculteurs', 'money': 100030, 'score': 100030, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 1, 'LEEK': 2, 'TOMATO': 3, 'ONION': 4, 'ZUCCHINI': 5}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}]}
    aigrisculteurs.get_my_farm_json()
    assert(aigrisculteurs.check_if_field_sown(1) == False)
    
    aigrisculteurs.game_data = {'day': 0, 'greenhouse_gas': 0, 'events': [], 'farms': [{'blocked': False, 'name': 'aigrisculteurs', 'money': 100030, 'score': 100030, 'fields': [{'content': 'POTATO', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 1, 'LEEK': 2, 'TOMATO': 3, 'ONION': 4, 'ZUCCHINI': 5}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}]}
    aigrisculteurs.get_my_farm_json()
    assert(aigrisculteurs.check_if_field_sown(1) == True)

def test_worker_sow_vegetable_at_field(aigrisculteurs):
    aigrisculteurs.hiring_workers(1)
    aigrisculteurs.worker_sow_vegetable_at_field(1, TOMATO[1],1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 SEMER TOMATE 1"

    aigrisculteurs.worker_sow_vegetable_at_field(1, 'CITROUILLE',1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1]) == "1 SEMER TOMATE 1"

def test_less_stocked_vegetable(aigrisculteurs):
    aigrisculteurs.game_data = {'day': 0, 'greenhouse_gas': 0, 'events': [], 'farms': [{'blocked': False, 'name': 'aigrisculteurs', 'money': 100030, 'score': 100030, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 1, 'LEEK': 2, 'TOMATO': 3, 'ONION': 4, 'ZUCCHINI': 5}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}]}
    aigrisculteurs.get_my_farm_json()
    logging.debug(f"Less stocked vegetables {aigrisculteurs.get_less_stocked_vegetable()}")
    assert(aigrisculteurs.get_less_stocked_vegetable() == "PATATE")

def test_seed_less_stocked_vegetable(aigrisculteurs):
    aigrisculteurs.game_data = {'day': 0, 'greenhouse_gas': 0, 'events': [], 'farms': [{'blocked': False, 'name': 'aigrisculteurs', 'money': 100030, 'score': 100030, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 1, 'LEEK': 2, 'TOMATO': 3, 'ONION': 4, 'ZUCCHINI': 5}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}, {'blocked': True, 'name': '', 'money': 100000, 'score': 100000, 'fields': [{'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD1'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD2'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD3'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD4'}, {'content': 'NONE', 'needed_water': 0, 'bought': False, 'location': 'FIELD5'}], 'tractors': [], 'loans': [], 'soup_factory': {'days_off': 0, 'stock': {'POTATO': 0, 'LEEK': 0, 'TOMATO': 0, 'ONION': 0, 'ZUCCHINI': 0}}, 'employees': [], 'events': []}]}
    aigrisculteurs.get_my_farm_json()
    aigrisculteurs.hiring_workers(1)
    logging.debug(f"NUMBER OF EMPLOYEE {aigrisculteurs.actual_number_of_workers}")

    aigrisculteurs.seed_less_stocked_vegetable(1,1)
    assert (aigrisculteurs.aigrisculteurs_commands[-1] == "1 SEMER PATATE 1")

