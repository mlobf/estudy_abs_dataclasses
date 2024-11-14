import pytest
import json
from ..implementacao import BonusNonMonetaryFinancialController
from ..dataclasses_base.dataclass import DataBonusNonMonetaryFinancialController


# Carregar dados do JSON uma vez para usar em todos os testes
with open("tests/fixtures.json", "r") as file:
    test_data = json.load(file)


# Fixture parametrizada para criar uma instância do controlador com cada conjunto de dados
@pytest.fixture(params=test_data)
def controller(request):
    data = request.param
    return BonusNonMonetaryFinancialController(
        last_prize=data["last_prize"],
        free_games_award=data["free_games_award"],
        free_games_balance=data["free_games_balance"],
    )


# Teste para o método is_refundable
@pytest.mark.parametrize("data", test_data)
def test_is_refundable(data):
    controller = BonusNonMonetaryFinancialController(
        last_prize=data["last_prize"],
        free_games_award=data["free_games_award"],
        free_games_balance=data["free_games_balance"],
    )
    expected_result = data["last_prize"] > 0 and bool(data["free_games_award"])
    assert controller.is_refundable() == expected_result


# Teste para o método deduct_from_prize com valor válido
@pytest.mark.parametrize("data", test_data)
def test_deduct_from_prize(data):
    controller = BonusNonMonetaryFinancialController(
        last_prize=data["last_prize"],
        free_games_award=data["free_games_award"],
        free_games_balance=data["free_games_balance"],
    )
    if data["last_prize"] >= 10.0:
        remaining_prize = controller.deduct_from_prize(10.0)
        assert remaining_prize == data["last_prize"] - 10.0
    else:
        with pytest.raises(
            ValueError, match="O valor a ser deduzido excede o prêmio atual."
        ):
            controller.deduct_from_prize(10.0)


# Teste para o método set_cache
@pytest.mark.parametrize("data", test_data)
def test_set_cache(data, capsys):
    controller = BonusNonMonetaryFinancialController(
        last_prize=data["last_prize"],
        free_games_award=data["free_games_award"],
        free_games_balance=data["free_games_balance"],
    )
    result = controller.set_cache()
    captured = capsys.readouterr()
    assert result is True
    assert "Dados armazenados em cache." in captured.out  # Verifica a saída do print


# Teste para o método del_cache
@pytest.mark.parametrize("data", test_data)
def test_del_cache(data, capsys):
    controller = BonusNonMonetaryFinancialController(
        last_prize=data["last_prize"],
        free_games_award=data["free_games_award"],
        free_games_balance=data["free_games_balance"],
    )
    result = controller.del_cache()
    captured = capsys.readouterr()
    assert result is True
    assert "Cache removido." in captured.out  # Verifica a saída do print


# Teste para o método set_nosql
@pytest.mark.parametrize("data", test_data)
def test_set_nosql(data, capsys):
    controller = BonusNonMonetaryFinancialController(
        last_prize=data["last_prize"],
        free_games_award=data["free_games_award"],
        free_games_balance=data["free_games_balance"],
    )
    result = controller.set_nosql()
    captured = capsys.readouterr()
    assert result is True
    assert (
        "Dados armazenados no banco NoSQL." in captured.out
    )  # Verifica a saída do print
