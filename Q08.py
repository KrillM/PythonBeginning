# N18 ~ 22

class House:
    def __init__(self, location, house_type, deal_type, price, construction_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.construction_year = construction_year

    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.construction_year))


GangNam = House("강남", "아파트", "매매", "10억", "2010년")
Mapo = House("마포", "오피스텔", "전세", "5억", "2007년")
SongPa = House("송파", "빌라", "월세", "500/50", "2000년")

GangNam.show_detail()
Mapo.show_detail()
SongPa.show_detail()