class ATM:
    def __init__(self):
        self.cash = [0, 0, 0, 0, 0]
        self.denominations = [20, 50, 100, 200, 500]

    def deposit(self, deposited_amounts: List[int]) -> None:
        for i in range(len(deposited_amounts)):
            self.cash[i] += deposited_amounts[i]

    def withdraw(self, withdrawal_amount: int) -> List[int]:
        result = [0, 0, 0, 0, 0]

        for i in range(4, -1, -1):
            available_notes = self.cash[i]
            denomination_value = self.denominations[i]

            notes_to_withdraw = min(available_notes, withdrawal_amount // denomination_value)
            result[i] = notes_to_withdraw
            withdrawal_amount -= (notes_to_withdraw * denomination_value)

        if withdrawal_amount == 0:
            self.deposit([-notes for notes in result])
            return result
        else:
            return [-1]
