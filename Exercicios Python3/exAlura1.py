class CharacterRPG:
    def __init__(self, nickname, race, classe, power):
        self.__nickname__ = nickname
        self.__race__ = race
        self.__classe__ = classe
        self.__superPower__ = power

    @property
    def nickname(self):
        return self.__nickname__

    @property
    def race(self):
        return self.__race__

    @property
    def classe(self):
        return self.__classe__

    @property
    def superPower(self):
        return self.__superPower__

    @nickname.setter
    def nickname(self, nickname):
        self.__nickname__ = nickname

    @race.setter
    def race(self, race):
        self.__race__ = race

    @classe.setter
    def classe(self, classe):
        self.__classe__ = classe

    @superPower.setter
    def superPower(self, power):
        self.__superPower__ = power
