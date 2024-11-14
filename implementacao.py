import logging
from dataclasses_base.dataclass import (
    DataBonusNonMonetaryFinancialController,
)
from abstract_classes_base.base_abstract import BaseBonusNonMonetaryFinancialController

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BonusNonMonetaryFinancialController(BaseBonusNonMonetaryFinancialController):

    def __init__(self, data: DataBonusNonMonetaryFinancialController) -> None:

        self.last_prize = data.last_prize
        self.free_games_award = data.award_list
        self.free_games_balance = data.free_games_balance

        logger.info(
            """Instância de BonusNonMonetaryFinancialController criada \n 
            com last_prize=%s, free_games_award=%s, free_games_balance=%s""",
            data.last_prize,
            data.free_games_award,
            data.free_games_balance,
        )

    def set_last_prize(self, new_last_prize_value: float) -> float:
        """Atualiza o valor do prêmio. Apenas um simples test."""
        if new_last_prize_value < 0:
            logger.error("O valor do prêmio não pode ser negativo.")
            raise ValueError("O valor do prêmio não pode ser negativo.")
        self.last_prize = new_last_prize_value
        logger.info("Novo valor de prêmio setado: %s", self.last_prize)
        return self.last_prize

    def is_refundable(self) -> bool:
        """Verifica se houve ocorrência da situação passível de estorno."""
        result = self.last_prize > 0 and bool(self.free_games_award_list)
        logger.info("Método is_refundable executado com resultado: %s", result)
        return result

    def deduct_from_prize(self, amount: float) -> float:
        """Deduz um valor do prêmio atual e retorna o saldo."""
        try:
            if amount > self.last_prize:
                logger.warning(
                    "Tentativa de deduzir um valor maior que o prêmio atual: amount=%s, last_prize=%s",
                    amount,
                    self.last_prize,
                )
                raise ValueError("O valor a ser deduzido excede o prêmio atual.")
            self.last_prize -= amount
            logger.info(
                "Valor deduzido com sucesso. Novo last_prize=%s", self.last_prize
            )
            return self.last_prize
        except ValueError as e:
            logger.error("Erro ao deduzir valor: %s", e)
            raise
        except Exception as e:
            logger.error("Erro inesperado em deduct_from_prize: %s", e)
            raise

    def set_cache(self) -> bool:
        """Simula a configuração de cache para os dados do prêmio."""
        try:
            # Exemplo de lógica para armazenar no cache
            print("Dados armazenados em cache.")
            logger.info("Cache configurado com sucesso.")
            return True
        except Exception as e:
            logger.error("Erro ao configurar o cache: %s", e)
            raise

    def del_cache(self) -> bool:
        """Remove o cache dos dados do prêmio."""
        try:
            # Exemplo de lógica para remover do cache
            print("Cache removido.")
            logger.info("Cache removido com sucesso.")
            return True
        except Exception as e:
            logger.error("Erro ao remover o cache: %s", e)
            raise

    def set_nosql(self) -> bool:
        """Salva dados em um banco NoSQL (simulação)."""
        try:
            # Exemplo de lógica para salvar no banco NoSQL
            print("Dados armazenados no banco NoSQL.")
            logger.info("Dados armazenados no banco NoSQL com sucesso.")
            return True
        except Exception as e:
            logger.error("Erro ao armazenar dados no banco NoSQL: %s", e)
            raise

    def say_hi(self):
        return print("hi")


class OutroBonus(BonusNonMonetaryFinancialController): ...
