from math import hypot
from math import pi


class Bod:
    def __init__(self, *_arg):
        if len(_arg) == 0:
            self.X = int(input("Zadajte suradnicu X: "))
            self.Y = int(input("Zadajte suradnicu Y: "))
        elif len(_arg) == 1:
            self.X = _arg[0]
            self.Y = int(input("Zadajte suradnicu Y: "))
        else:
            self.X = _arg[0]
            self.Y = _arg[1]

    def get_distance(self, other):
        return hypot(self.X - other.X, self.Y - other.Y)

    @staticmethod
    def get_distance_static(_a, _b):
        return hypot(_a.X - _b.X, _a.Y - _b.Y)

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Bod(self.X + other, self.Y + other)
        elif isinstance(other, Bod):
            return Bod(self.X + other.X, self.Y + other.Y)

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Bod(self.X - other, self.Y - other)
        elif isinstance(other, Bod):
            return Bod(self.X - other.X, self.Y - other.Y)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Bod(self.X * other, self.Y * other)

    def __str__(self):
        return "[{}, {}]".format(self.X, self.Y)


class Trojuholnik:
    def __init__(self, _b1, _b2, _b3):
        self.A = _b1
        self.B = _b2
        self.C = _b3

        if self.exists():
            self.DlzkyStran = {"a": Bod.get_distance_static(self.B, self.C),
                               "b": Bod.get_distance_static(self.A, self.C),
                               "c": Bod.get_distance_static(self.A, self.B)}

            self.Strany = {"a": Priamka(self.B, self.C),
                           "b": Priamka(self.A, self.C),
                           "c": Priamka(self.A, self.B)}

            self.Obvod = self.get_obvod()

            self.Obsah = self.get_obsah()

            self.Tazisko = self.get_tazisko()

    def __str__(self):
        return "Trojuholnik {} {} {} \n" \
               "  Strany: {} {} {}".format(self.A, self.B, self.C,
                                           self.DlzkyStran["a"], self.DlzkyStran["b"], self.DlzkyStran["c"])

    def exists(self):
        vektor1 = Bod(self.B.X - self.A.X, self.B.Y - self.A.Y)
        vektor2 = Bod(self.C.X - self.A.Y, self.C.Y - self.A.Y)

        k1 = (vektor1.X / vektor2.X) if vektor2.X != 0 else 0
        k2 = (vektor1.Y / vektor2.Y) if vektor2.Y != 0 else 0

        return not k1 == k2

    def get_strana(self, _strana):
        try:
            _strana = _strana.lower()
            if _strana not in "abc":
                raise AttributeError

        except AttributeError:
            print("Zly vstup strany! \n Povolene vstupy: A, B, C (a, b, c)")
            return

        return self.DlzkyStran[_strana]

    def get_obvod(self):
        return sum(self.DlzkyStran.values())

    def get_obsah(self):
        s = self.Obvod / 2
        return (s * (s - self.DlzkyStran["a"]) * (s - self.DlzkyStran["b"]) * (s - self.DlzkyStran["c"])) ** (1/2)

    def get_tazisko(self):
        return Bod((self.A.X + self.B.X + self.C.X) * (1 / 3), (self.A.Y + self.B.Y + self.C.Y) * (1 / 3))


class Kruznica:
    def __init__(self, _r):
        self.Polomer = _r
        self.Obvod = self.get_obvod()
        self.Obsah = self.get_obsah()

    def get_obvod(self):
        return 2 * pi * self.Polomer

    def get_obsah(self):
        return pi * (self.Polomer ** 2)

    def __str__(self):
        return "Kruznica; r = {}; O = {}; S = {}".format(self.Polomer, self.Obvod, self.Obsah)


class Priamka:
    def __init__(self, _b1, _b2):
        self.A = _b1
        self.B = _b2
        self.Dlzka = self.get_dlzka()
        self.Stred = self.get_stred()

    def __str__(self):
        return "Priamka; A = {}; B = {}; Dlzka = {}".format(self.A, self.B, self.Dlzka)

    def get_dlzka(self):
        return Bod.get_distance_static(self.A, self.B)

    def get_stred(self):
        return (self.A - self.B) / 2

