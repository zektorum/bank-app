from dataclasses import dataclass


@dataclass
class Deposit:
    type: str
    amount: float
    date: str
