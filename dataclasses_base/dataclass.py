"""Just a simple collection of dataclasses to be used as data interface"""

from typing import List
from dataclasses import dataclass


@dataclass
class FreeGamesAward:
    award_list: List[int]


@dataclass
class DataBonusNonMonetaryFinancialController:
    last_prize: float
    free_games_award: FreeGamesAward
    free_games_balance: float
