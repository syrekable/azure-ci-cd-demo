class Eggs:
    def __init__(self, spam) -> None:
        self.spam = spam

class Spam:
    def __init__(self) -> None:
        self.name = "Spam"

def foo(spam: Spam) -> Eggs:
    eggs = Eggs(spam= spam)
    return eggs