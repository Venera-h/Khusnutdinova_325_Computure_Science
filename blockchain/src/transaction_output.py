from typing import Dict, Any

class TransactionOutput:
    def __init__(self, recipient: str, amount: float):
        self.recipient = recipient  # Адрес получателя
        self.amount = amount  # Сумма перевода
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            'recipient': self.recipient,
            'amount': self.amount
        }