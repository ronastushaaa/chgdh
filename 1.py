class k:
    def __new__(k):
        print('hjkhj')

    def __init__(self, data):
        self.next_obj = None
        self.data = data

    def link(self, obj):
        self.next_obj = obj

lst_in = list(map(str.strip, sys.strip.readlines)

