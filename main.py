"""Implementacao da Classe BonusNonMonetaryFinancialController"""

from implementacao import BonusNonMonetaryFinancialController
from dataclasses_base.dataclass import (
    FreeGamesAward,
    DataBonusNonMonetaryFinancialController,
)

if __name__ == "__main__":
    # try:
    minha_lista = [10, 30, 30]
    payload = [
        100,
        FreeGamesAward(minha_lista),
        50,
    ]

    controller = BonusNonMonetaryFinancialController(
        data=DataBonusNonMonetaryFinancialController(*payload)
    )

    print(controller.is_refundable())
    print(controller.deduct_from_prize(10))
    controller.set_cache()
    controller.del_cache()
    controller.set_nosql()

    # except Exception as e:
    #    logger.critical("Erro crítico na execução principal: %s", e)
