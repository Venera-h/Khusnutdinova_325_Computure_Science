import hashlib
import json
from typing import List, Dict, Any
from  transaction_input import TransactionInput
from transaction_output import TransactionOutput

class Transaction:
    def __init__(self, inputs: List[TransactionInput], outputs: List[TransactionOutput], signature: str = None):
        self.inputs = inputs  # Список входов транзакции
        self.outputs = outputs  # Список выходов транзакции
        self.signature = signature  # Цифровая подпись транзакции
        self.tx_id = self.calculate_hash()  # Уникальный идентификатор транзакции
        
    def calculate_hash(self) -> str:
        tx_data = {
            'inputs': [input.to_dict() for input in self.inputs],
            'outputs': [output.to_dict() for output in self.outputs]
        }
        tx_string = json.dumps(tx_data, sort_keys=True).encode()
        return hashlib.sha256(tx_string).hexdigest()
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            'tx_id': self.tx_id,
            'inputs': [input.to_dict() for input in self.inputs],
            'outputs': [output.to_dict() for output in self.outputs],
            'signature': self.signature
        }
        
    def sign(self, signature: str) -> None:
        self.signature = signature
        
    def verify(self) -> bool:
        return self.signature is not None
        
    @classmethod
    def from_dict(cls, tx_dict: Dict[str, Any]) -> 'Transaction':
        inputs = [TransactionInput(input['tx_id'], input['output_index']) 
                 for input in tx_dict['inputs']]
        outputs = [TransactionOutput(output['recipient'], output['amount']) 
                  for output in tx_dict['outputs']]
        tx = cls(inputs, outputs, tx_dict.get('signature'))
        tx.tx_id = tx_dict['tx_id']
        return tx