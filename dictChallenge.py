transactions = [
    {"id": 1, "type": "credit", "amount": 5000, "category": "salary"},
    {"id": 2, "type": "debit", "amount": 1500, "category": "rent"},
    {"id": 3, "type": "debit", "amount": 500, "category": "food"},
    {"id": 4, "type": "credit", "amount": 2000, "category": "freelance"},
    {"id": 5, "type": "debit", "amount": 700, "category": "food"},
]

def highestDebit(tran : list[dict]) -> dict:
    highest = 0
    dictionary = {}

    for dic in tran:
      if dic['type'] == 'debit':
          if dic['amount'] > highest:
            highest = dic['amount']
            dictionary = {
                "id": dic['id'],
                "type":dic['type'],
                "amount":dic['amount'],
                "category":dic["category"]
            }

    return dictionary

def totalSpend(trans: list[dict]) -> dict:
    salary = 0 ; rent = 0 ; food = 0 ; freelance = 0
    for dic in trans:
        if dic['category'] == 'salary':
            salary += dic['amount']
        elif dic['category'] == 'rent':
            rent += dic['amount']
        elif dic['category'] == 'food':
            food += dic['amount']
        elif dic['category'] == 'freelance':
            freelance += dic['amount']
    return {
        "food" : food ,
        "salary":salary,
        "rent" : rent,
        "freelance" : freelance
    }


def checkFraud(trans : list[dict]) -> bool:
    fraud_status = False

    for dic in trans:
        if dic['type'] == 'debit':
            if dic['amount'] > 3000:
                fraud_status = True 

    return fraud_status


def analyze_transactions(transactions: list[dict]) -> dict:
    credit = 0
    debit = 0
    for dic in transactions:
        if dic['type'] == 'credit':
            credit = credit + dic['amount']
        else:
            debit = debit + dic['amount']

    total_balance = credit - debit

    total_spend_perCato: dict = totalSpend(transactions)
    highest_single_debit_transaction: dict = highestDebit(transactions)
    setFraud: bool = checkFraud(transactions)

    return{
        "total_balance":total_balance,
        "totalSpend_Per_Category":total_spend_perCato,
        "highest_SingleDebit":highest_single_debit_transaction,
        "Fraud_Status":setFraud   
    }

 
print(analyze_transactions(transactions))