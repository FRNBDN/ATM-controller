cards = [
    {
        "Owner": "John Doe",
        "Number": "1234567812345678",
        "PIN": "1234",
        "Accounts": [
            {"Name": "Checking", "Balance": 500},
            {"Name": "Savings", "Balance": 10000},
        ],
    },
    {
        "Owner": "Jane Smith",
        "Number": "9876543210987654",
        "PIN": "4321",
        "Accounts": [
            {"Name": "Checking", "Balance": 1200},
            {"Name": "Savings", "Balance": 15000},
        ],
    },
    {
        "Owner": "Sarah Johnson",
        "Number": "5678901256789012",
        "PIN": "2468",
        "Accounts": [
            {"Name": "Checking", "Balance": 800},
            {"Name": "Savings", "Balance": 5000},
        ],
    },
    {
        "Owner": "Michael Brown",
        "Number": "3456789034567890",
        "PIN": "9876",
        "Accounts": [
            {"Name": "Checking", "Balance": 1500},
            {"Name": "Savings", "Balance": 20000},
        ],
    },
]

current_card = {
    "Owner": "",
    "Number": "",
    "Accounts": [],
}


def validate_card_nr(card_nr):
    for card in cards:
        if card["Number"] == card_nr:
            return card_nr
    return None


def verify_pin(card_nr, pin):
    for card in cards:
        if card["Number"] == card_nr:
            if card["PIN"] == pin:
                return True
    return False


def fetch_accounts_data(card_nr):
    for card in cards:
        if card["Number"] == card_nr:
            return [card["Accounts"], card["Owner"]]

    return "Failed to retrieve information"


def account_actions(account_idx, action):
    account = current_card["Accounts"][int(account_idx)]
    if action == "Check Balance":
        print(account["Balance"])
    elif action == "Deposit":
        deposit(account)
    elif action == "Withdraw":
        withdraw(account)
    else:
        print("error")


def deposit(account):
    value_deposited = int(input("Input value deposited to account: \n $"))
    account["Balance"] += value_deposited
    print(account["Balance"])
    for prev_account in current_card["Accounts"]:
        if prev_account["Name"] == account["Name"]:
            prev_account["Balance"] = account["Balance"]


def withdraw(account):
    value_withdrawn = int(input("Input value you wish to withdraw: \n $"))
    if value_withdrawn > account["Balance"]:
        print("Insufficient Funds")

    else:
        account["Balance"] -= value_withdrawn
        print(account["Balance"])
        for prev_account in current_card["Accounts"]:
            if prev_account["Name"] == account["Name"]:
                prev_account["Balance"] = account["Balance"]


mock_card = "3456789034567890"

inserted_card = validate_card_nr(mock_card)
if inserted_card:
    current_card["Number"] = inserted_card
    trials = 3
    while trials > 0:
        pin = input("Input PIN Code: ")
        validated_pin = verify_pin(inserted_card, pin)
        if validated_pin:
            accounts_data = fetch_accounts_data(current_card["Number"])
            current_card["Accounts"] = accounts_data[0]
            current_card["Owner"] = accounts_data[1]
            break
        else:
            trials -= 1
    print("Choose Account")
    choices = []
    account_choice = ""
    for index, account in enumerate(current_card["Accounts"]):
        print(f"{index}: {account['Name']}")
        choices.append(str(index))
    while account_choice not in choices:
        account_choice = input("")
        if account_choice not in choices:
            print("invalid input, try again")
    print("Choose Action")
    action_choice = input("")

    account_actions(account_choice, action_choice)
    update_account()
