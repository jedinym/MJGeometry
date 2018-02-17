from math import hypot


class Bod:
    def __init__(self, *arg):
        if len(arg) == 0:
            self.X = int(input("Zadajte suradnicu X: "))
            self.Y = int(input("Zadajte suradnicu Y: "))
        elif len(arg) == 1:
            self.X = arg[0]
            self.Y = int(input("Zadajte suradnicu Y: "))
        else:
            self.X = arg[0]
            self.Y = arg[1]

    def get_distance(self, other):
        return hypot(self.X - other.X, self.Y - other.Y)

    @staticmethod
    def get_distance_static(_a, _b):
        return hypot(_a.X - _b.X, _a.Y - _b.Y)

    def __add__(self, other):
        if isinstance(other, int):
            return Bod(self.X + other, self.Y + other)
        elif isinstance(other, Bod):
            return Bod(self.X + other.X, self.Y + other.Y)

    def __sub__(self, other):
        if isinstance(other, int):
            return Bod(self.X - other, self.Y - other)
        elif isinstance(other, Bod):
            return Bod(self.X - other.X, self.Y - other.Y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Bod(self.X * other, self.Y * other)

    def __str__(self):
        return "[{}, {}]".format(self.X, self.Y)


class Trojuholnik:
    def __init__(self, _b1, _b2, _b3):
        self.A = _b1
        self.B = _b2
        self.C = _b3

        # self.StranaA = Bod.get_distance_static(self.B, self.C)
        # self.StranaB = Bod.get_distance_static(self.A, self.C)
        # self.StranaC = Bod.get_distance_static(self.A, self.B)

        if self.exists():
            self.Strany = {"a": Bod.get_distance_static(self.B, self.C),
                           "b": Bod.get_distance_static(self.A, self.C),
                           "c": Bod.get_distance_static(self.A, self.B)}

            self.Obvod = self.get_obvod()
            self.Obsah = self.get_obsah()

    def __str__(self):
        return "Trojuholnik {} {} {} \n" \
               "  Strany: {} {} {}".format(self.A, self.B, self.C, self.Strany["a"], self.Strany["b"], self.Strany["c"])

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

        return self.Strany[_strana]

    def get_obvod(self):
        return sum(self.Strany.values())

    def get_obsah(self):
        s = self.Obvod / 2
        return (s * (s - self.Strany["a"]) * (s - self.Strany["b"]) * (s - self.Strany["c"])) ** (1/2)


