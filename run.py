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


def deposit(account, value_deposited):
    """
    Function handling deposits, input value as a placeholder.
    """
    if value_deposited <= 0:
        raise ValueError("Invalid deposit amount")
    account["Balance"] += value_deposited


def withdraw(account, value_withdrawn):
    """
    Function for withdrawing funds, checks if the account
    has the necessary funds before witdrawing.
    """
    if value_withdrawn <= 0:
        raise ValueError("Invalid withdrawal amount")
    if value_withdrawn > account["Balance"]:
        raise ValueError("Insufficient funds")
    account["Balance"] -= value_withdrawn


def update_account():
    """
    Funciton that updates the new balance information for the card,
    API PUT request here.
    """
    for card in CARDS:
        if card["Number"] == current_card["Number"]:
            card.update(current_card)


def main():
    """
    Main fuction running all program functions.
    """
    inserted_card = validate_card_nr("3456789034567890")
    if inserted_card:
        current_card["Number"] = inserted_card
        trials = 3
        while trials > 0:
            validate_pin = verify_pin(inserted_card, "9876")
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
            account_choice = "0"  # User input
            if account_choice not in choices:
                raise ValueError("Invalid option")
        action_choice = "Check Balance"  # User input

        selected_account = current_card["Accounts"][int(account_choice)]
        if action_choice == "Check Balance":
            print(selected_account["Balance"])
        elif action_choice == "Deposit":
            value_deposited = 100  # User input
            deposit(selected_account, value_deposited)
        elif action_choice == "Withdraw":
            value_withdrawn = 200  # User input
            withdraw(selected_account, value_withdrawn)
        else:
            raise ValueError("Invalid option")

        update_account()


main()
