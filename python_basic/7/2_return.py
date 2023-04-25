def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposite(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance + money}")
    return balance + money


def withdraw(balnace, money):
    if balnace >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balnace - money}")
        return balnace - money
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balnace}")
        return balnace


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposite(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 300)
commission, balance = withdraw_night(balance, 500)
print(f"수수료 {commission} 원이며, 잔액은 {balance} 원입니다.")
