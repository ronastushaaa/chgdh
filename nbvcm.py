from string import ascii_uppercase, digits


class CardChecker:
    CHARS_FOR_NAME = string.ascii_uppercase + digits + ' '

    @staticmethod
    def check_card_numder(number):
       return len( [i.isdigit() for i in number.split('-') if len(i) ==4]) == 4

    @classmethod
    def check_name(cls, name):
        return all([[True if j in cls.CHARS_FOR_NAME else False for j in i] for i in name.split()])

is_number = CardChecker.check_card_numder('123-456-789-0000')
is_name = CardChecker.check_name()


