from abc import ABC, abstractmethod

class MiniProgramBase(ABC):
    def __init__(self, accounts):
        self.accounts = accounts

    @abstractmethod
    def sign(self, account):
        pass

    def run_all(self):
        for account in self.accounts:
            try:
                self.sign(account)
            except Exception as e:
                print(f"[{self.__class__.__name__}] 账号 {account.get('name')} 异常: {e}")