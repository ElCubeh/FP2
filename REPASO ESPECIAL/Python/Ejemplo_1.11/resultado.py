class Transaction:
    def __init__(self, type, amount, timestamp):
        self.type = type
        self.amount = amount
        self.timestamp = timestamp

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class AccountBase:
    def __init__(self):
        self.first = None
        self._size = 0

    def get_transaction(self, index):
        if not (0 <= index < self._size): return None
        current = self.first
        for _ in range(index):
            current = current.next
        return current.value
    
    def get_size(self):
        return self._size

class BankAccount(AccountBase):
    _total_assets = 0.0

    def __init__(self, owner, account_number, initial_balance=0.0):
        super().__init__()
        self.owner = owner
        self.account_number = account_number
        self._balance = initial_balance
        BankAccount._total_assets += initial_balance

    def add_transaction(self, transaction):
        new_balance = self._balance
        if transaction.type == "depósito":
            new_balance += transaction.amount
        elif transaction.type == "retirada":
            new_balance -= transaction.amount
        
        if new_balance < 0:
            return False

        new_node = Node(transaction)
        if self.first is None: self.first = new_node
        else:
            curr = self.first
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1
        
        BankAccount._total_assets += (new_balance - self._balance)
        self._balance = new_balance
        return True

    @property
    def balance(self):
        return self._balance

    def get_deposits(self):
        deposits = []
        curr = self.first
        while curr:
            if curr.value.type == "depósito":
                deposits.append(curr.value)
            curr = curr.next
        return deposits

    @classmethod
    def get_total_assets(cls):
        return cls._total_assets