"""ATM-controller Project"""

CARDS = [  # Cards and details, as a mock API
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

MOCK_CARD = "3456789034567890"
USER_INPUT_PIN = "9876"


def validate_card_nr(card_nr):
    """
    Checks if the card is a valid number,
    Here the API Request would be made for seeing if
    the Card is valid
    """
    if not card_nr.isnumeric():
        raise ValueError("Invalid card number format")

    for card in CARDS:
        if card["Number"] == card_nr:
            return card_nr
    return None


def verify_pin(card_nr, pin):
    """
    Checks if the PIN is exactly 4 digits and if correct and returns True/False,
    Here the API Request would be made for the PIN+Card Number
    """
    if len(pin) != 4 or not pin.isnumeric():
        raise ValueError("Invalid pin format")
    for card in CARDS:
        if card["Number"] == card_nr:
            if card["PIN"] == pin:
                return True
    return False


def fetch_accounts_data(card_nr):
    """
    Fetching the Accounts and Owner of the account,
    after PIN has been validated.
    """
    for card in CARDS:
        if card["Number"] == card_nr:
            return [card["Accounts"], card["Owner"]]
    return None


def account_actions(account_idx, action):
    """
    Takes the user inputs of account and action and
    calls function for the different actions for the
    account.
    """
    account = current_card["Accounts"][int(account_idx)]
    if action == "Check Balance":
        # Since the Balance is stored locally there is no
        # need for a function.
        print(account["Balance"])
    elif action == "Deposit":
        deposit(account)
    elif action == "Withdraw":
        withdraw(account)
    else:
        raise ValueError("Invalid option")
    return account


def deposit(account):
    """
    Function handling deposits, input value as a placeholder.
    """
    try:
        value_deposited = int(input("Input value deposited to account: \n $"))
        if value_deposited <= 0:
            raise ValueError("Invalid deposit amount")
        account["Balance"] += value_deposited
        for prev_account in current_card["Accounts"]:
            if prev_account["Name"] == account["Name"]:
                prev_account["Balance"] = account["Balance"]
    except ValueError as e:
        print(f"Error: {str(e)}")
    return account


def withdraw(account):
    """
    Function for withdrawing funds, checks if the account
    has the necessary funds before witdrawing.
    """
    value_withdrawn = int(input("Input value you wish to withdraw: \n $"))
    if value_withdrawn <= 0:
        raise ValueError("Invalid withdrawal amount")
    if value_withdrawn > account["Balance"]:
        raise ValueError("Insufficient funds")

    account["Balance"] -= value_withdrawn
    for prev_account in current_card["Accounts"]:
        if prev_account["Name"] == account["Name"]:
            prev_account["Balance"] = account["Balance"]
    return account


def update_account():
    """
    Funciton that updates the new balance information for the card,
    API PUT request here.
    """
    for card in CARDS:
        if card["Number"] == current_card["Number"]:
            card = current_card


def main():
    """
    Main fuction running all program functions.
    """
    inserted_card = validate_card_nr(MOCK_CARD)
    if inserted_card:
        current_card["Number"] = inserted_card
        trials = 3
        while trials > 0:
            validate_pin = verify_pin(inserted_card, USER_INPUT_PIN)
            if validate_pin:
                accounts_data = fetch_accounts_data(current_card["Number"])
                current_card["Accounts"] = accounts_data[0]
                current_card["Owner"] = accounts_data[1]
                break

            trials -= 1
        choices = []
        account_choice = ""
        for index, account in enumerate(current_card["Accounts"]):
            print(f"{index}: {account['Name']}")
            choices.append(str(index))
        while account_choice not in choices:
            account_choice = input("Choose Account:\n")
            if account_choice not in choices:
                raise ValueError("Invalid option")
        action_choice = input("Choose Action:\n")

        account_actions(account_choice, action_choice)
        update_account()


main()
