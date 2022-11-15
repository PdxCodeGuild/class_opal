# Lab 14: Test ATM
from atm import ATM


balance = 0
deposit = 10.0
interest_rate = 0.1

def test_atm():
    assert balance is 0
    assert balance + deposit == 10.0
