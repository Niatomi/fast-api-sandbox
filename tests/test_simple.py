import pytest

from src.__main__ import inc as func

@pytest.mark.parametrize("num1, expected", [
    (3, 4),
    (2, 3),
    (5, 6),
    (10, 11),
])
def test_inc(num1, expected):
    assert func(num1) == expected


class BankAccount():
    
    def __init__(self, balance: int = 0, annual_prcentage: float = 1.1):
        self.balance = balance
        self.annual_prcentage = annual_prcentage
        
    def add_money(self, amount: int):
        self.balance += amount
        
    def withdraw_money(self, amount: int):
        check_balance = self.balance
        check_balance -= amount
        if check_balance < 0:
            raise Exception
        self.balance = check_balance
    
    def add_annual(self):
        self.balance *= self.annual_prcentage

BALACE = 50

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(BALACE)
        
def test_account_create_1(zero_bank_account):
    assert zero_bank_account.balance == 0
    
def test_account_create_2(bank_account):
    assert bank_account.balance == BALACE
    

@pytest.mark.parametrize("deposit, withdraw, expected", [
    (100, 50, 50),
    (100, 40, 60),
    (300, 500, Exception),
])
def test_withdraw_test(zero_bank_account: BankAccount, deposit, withdraw, expected):
    zero_bank_account.add_money(deposit)
    if expected is Exception:
        with pytest.raises(Exception):
            zero_bank_account.withdraw_money(withdraw)
    else:
            zero_bank_account.withdraw_money(withdraw)
            assert zero_bank_account.balance == expected
        