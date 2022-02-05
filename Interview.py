class Stack():
    def __init__(self, my_str):
        self.my_str = my_str

    def isEmpty(self):
        if len(self.my_str) != 0:
            return True
        else:
            return False

    def push(self, s_add):
        self.my_str = self.my_str + s_add

    def pop(self):
        self.my_str = self.my_str[:len(self.my_str)-1]
        return self.my_str[-1]

    def peek(self):
        return self.my_str[-1]

    def size(self):
        return len(self.my_str)

    def is_balance(self):
        if self.my_str.count('(') == self.my_str.count(')') and self.my_str.count('{') == self.my_str.count('}')\
                and self.my_str.count('[') == self.my_str.count(']'):
            return 'Сбалансировано'
        else:
            return ' Не сбалансировано'

print(Stack('(((({}]))))').is_balance())