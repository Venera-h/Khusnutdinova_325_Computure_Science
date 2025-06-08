from typing import Dict, Any

class TransactionInput:
    def __init__(self, tx_id: str, output_index: int):
        self.tx_id = tx_id  # ID предыдущей транзакции
        self.output_index = output_index  # Индекс выхода в предыдущей транзакции
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            'tx_id': self.tx_id,
            'output_index': self.output_index
        }