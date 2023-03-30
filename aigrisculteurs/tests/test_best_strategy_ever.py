from src.best_startegy_ever import Aigrisculteurs
import pytest


@pytest.fixture
def aigrisculteurs():
    return Aigrisculteurs()


def test_buy_fields(aigrisculteurs):
    aigrisculteurs.buy_fields(2)
    assert (aigrisculteurs.number_of_fields) == 2
    aigrisculteurs.buy_fields(1)
    assert (aigrisculteurs.number_of_fields) == 3
    aigrisculteurs.buy_fields(600)
    assert (aigrisculteurs.number_of_fields) == 5
