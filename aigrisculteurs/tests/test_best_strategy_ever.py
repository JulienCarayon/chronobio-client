from src.best_startegy_ever import Aigrisculteurs
import pytest


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