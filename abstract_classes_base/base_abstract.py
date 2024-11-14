"""Just a simple collection of abstract classes to be used as
behavor interface"""

from abc import ABC, abstractmethod


class BaseBonusNonMonetaryFinancialController(ABC):

    @abstractmethod
    def set_last_prize(self):
        raise NotImplementedError("Should be extended only when implemented")

    @abstractmethod
    def is_refundable(self) -> bool:
        """Verifica se houve ocorrência da situação passível de estorno."""
        raise NotImplementedError("Should be extended only when implemented")

    @abstractmethod
    def deduct_from_prize(self, amount: float) -> float:
        """Deduz um valor do prêmio atual e retorna o saldo."""
        raise NotImplementedError("Should be extended only when implemented")

    @abstractmethod
    def set_cache(self) -> bool:
        """Simula a configuração de cache para os dados do prêmio."""
        raise NotImplementedError("Should be extended only when implemented")

    @abstractmethod
    def del_cache(self) -> bool:
        """Remove o cache dos dados do prêmio."""
        raise NotImplementedError("Should be extended only when implemented")

    @abstractmethod
    def set_nosql(self) -> bool:
        """Salva dados em um banco NoSQL (simulação)."""
        raise NotImplementedError("Should be extended only when implemented")
