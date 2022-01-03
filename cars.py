from datetime import date

info_file = open('data/informacje_najem.csv', 'r')
klienci = open('data/klienci.csv', 'r')
koszty = open('data/koszty.csv', 'r')
rezerwacje = open('data/rezerwacje.csv', 'r')
samochody = open('data/samochody.csv', 'r')
wypozyczenia = open('data/wypozyczenia.csv', 'r')

Infos = []
Clients = []
Costs = []
Reservations = []
Cars = []
Loans = []

def calcDays(strDate1, strDate2):
    date1Tab = strDate1.split('-')
    date2Tab = strDate2.split('-')
    date1 = date(int(date1Tab[0]), int(date1Tab[1]), int(date1Tab[2]))
    date2 = date(int(date2Tab[0]), int(date2Tab[1]), int(date2Tab[2]))
    return (date2 - date1).days

class Info():
    def __init__(self, id, cena, limitKm, kosztDodatkowy, idSamochodu):
        self.id = id
        self.cena = cena
        self.limitKm = limitKm
        self.kosztDodatkowy = kosztDodatkowy
        self.idSamochodu = idSamochodu

    def __str__(self):
        return str(self.__dict__)


class Klient():
    def __init__(self, idKlienta, nazwisko, wiek, prawoJazdyOd):
        self.idKlienta = idKlienta
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.prawoJazdyOd = prawoJazdyOd

    def __str__(self):
        return str(self.__dict__)


class Koszt():
    def __init__(self, idKosztu, dodatkoweKm, kosztNajmu, typPlatnosci, idWypozyczenia):
        self.idKosztu = idKosztu
        self.dodatkoweKm = dodatkoweKm
        self.kosztNajmu = kosztNajmu
        self.typPlatnosci = typPlatnosci
        self.idWypozyczenia = idWypozyczenia

    def __str__(self):
        return str(self.__dict__)


class Samochod():
    def __init__(self, idSamochodu, marka, moc, przyspieszenie):
        self.idSamochodu = idSamochodu
        self.marka = marka
        self.moc = moc
        self.przyspieszenie = przyspieszenie

    def __str__(self):
        return str(self.__dict__)


class Wypozyczenie():
    def __init__(self, idWypozyczenia, iloscKm, idRezerwacji):
        self.idWypozyczenia = idWypozyczenia
        self.iloscKm = iloscKm
        self.idRezerwacji = idRezerwacji

    def __str__(self):
        return str(self.__dict__)


class Rezerwacja():
    def __init__(self, idRezerwacji, dataRezerwacji, dataRozpoczecia, dataZakonczenia, idKlienta, idSamochodu):
        self.idRezerwacji = idRezerwacji
        self.dataRezerwacji = dataRezerwacji
        self.dataRozpoczecia = dataRozpoczecia
        self.dataZakonczenia = dataZakonczenia
        self.idKlienta = idKlienta
        self.idSamochodu = idSamochodu
        self.liczbaDni = calcDays(dataRozpoczecia, dataZakonczenia)

    def __str__(self):
        return str(self.__dict__)


for line in info_file:
    InfoData = line.split(',')
    newInfo = Info(InfoData[0], InfoData[1], InfoData[2], InfoData[3], InfoData[4][:-1:])
    Infos.append(newInfo)

for line in klienci:
    ClientData = line.split(',')
    newClient = Klient(ClientData[0], ClientData[1], ClientData[2], ClientData[3][:-1:])
    Clients.append(newClient)

for line in rezerwacje:
    ResData = line.split(',')
    newRes = Rezerwacja(ResData[0], ResData[1], ResData[2], ResData[3], ResData[4], ResData[5][:-1:])
    Reservations.append(newRes)
    
for line in koszty:
    CostData = line.split(',')
    newCost = Koszt(CostData[0], CostData[1], CostData[2], CostData[3], CostData[4][:-1:])
    Costs.append(newCost)
    
for line in samochody:
    CarData = line.split(',')
    newCar = Samochod(CarData[0], CarData[1], CarData[2], CarData[3][:-1:])
    Cars.append(newCar)
    
for line in wypozyczenia:
    LoanData = line.split(',')
    newLoan = Wypozyczenie(LoanData[0], LoanData[1], LoanData[2][:-1:])
    Loans.append(newLoan)

# calculate costs
for cost in Costs:
    for loan in Loans:
        if (loan.idWypozyczenia == cost.idWypozyczenia):
            przejechanychKm = int(loan.iloscKm)
            idRezerwacji = loan.idRezerwacji
    for reservation in Reservations:
        if (reservation.idRezerwacji == idRezerwacji):
            liczbaDni = int(reservation.liczbaDni)
            idSamochodu = reservation.idSamochodu
    for info in Infos:
        if (info.idSamochodu == idSamochodu):
            limit = int(info.limitKm)
            cena = int(info.cena)
            kosztDodatkowy = float(info.kosztDodatkowy)
    dodatkoweKm = przejechanychKm - liczbaDni*limit
    if(dodatkoweKm > 0):
        cost.dodatkoweKm = dodatkoweKm
    else:
        cost.dodatkoweKm = 0
    cost.kosztNajmu = cena*liczbaDni + cost.dodatkoweKm*kosztDodatkowy
    print(cost)
