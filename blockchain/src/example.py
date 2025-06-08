from transaction import Transaction, TransactionInput, TransactionOutput
import json

def main():
    input1 = TransactionInput("prev_tx_id_1", 0)
    input2 = TransactionInput("prev_tx_id_2", 1)
    
    output1 = TransactionOutput("recipient_address_1", 5.0)
    output2 = TransactionOutput("recipient_address_2", 3.5)
    
    tx = Transaction([input1, input2], [output1, output2])
    
    tx.sign("sample_signature_123")
    
    print(f"Transaction ID: {tx.tx_id}")
    print(f"Transaction verified: {tx.verify()}")
    
    tx_dict = tx.to_dict()
    print("Serialized transaction:", json.dumps(tx_dict, indent=2))
    
    tx_restored = Transaction.from_dict(tx_dict)
    print(f"Restored transaction ID: {tx_restored.tx_id}")

if __name__ == "__main__":
    main()