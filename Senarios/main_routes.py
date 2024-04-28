from base import Base
from Modules.profile import Profile
from Modules.search import Search
from Modules.result import Result
from Modules.revalidate import revalidate
from Modules.book import Book


from time import sleep
from helium import *

class MainRoutes(Base):
    def domestic_flight(self):
        Profile().login()
        sleep(2)
        Search().flight("domestic")
        Result().FlightResult().result()
        revalidate().domestic_flight()
        kill_browser()

    def international_flight(self):
        Profile().login()
        sleep(2)
        Search().flight("international")
        sleep(30)
        Result().FlightResult().result()
        revalidate().international_flight()
        kill_browser()
    def domestic_hotel(self):
        Profile().login()
        sleep(2)
        Search().hotel("domestic")
        # sleep(20)
        Result().HotelResult().result()
        Result().HotelResult().select_room()
        revalidate().domestic_hotel()
        sleep(2)
        Book().hotel()
        sleep(2)
        kill_browser()
    def international_hotel(self):
        Profile().login()
        sleep(2)
        Search().hotel("international")
        # sleep(20)
        Result().HotelResult().result()
        Result().HotelResult().select_room()
        sleep(13)
        revalidate().international_hotel()
        kill_browser()
    def train(self):
        Profile().login()
        sleep(2)
        Search().train()
        sleep(2)
        Result().TrainResult().result()
        sleep(2)
        revalidate().train()
        sleep(2)
        Book().train()
        kill_browser()

    def insurance(self):
        Profile().login()
        sleep(2)
        Search().insurance()
        sleep(2)
        Result().InsuranceResult().result()
        sleep(2)
        revalidate().insurance()
        sleep(2)
        Book().insurance()
        kill_browser()
    def tour(self):
        pass
    def visa(self):
        pass

if __name__ == "__main__":
    # driver = MainRoutes()
    # driver.domestic_flight()
    # sleep(10)
    # driver = MainRoutes()
    # driver.international_flight()
    # sleep(2)
    # driver = MainRoutes()
    # driver.domestic_hotel()
    # sleep(2)
    # driver = MainRoutes()
    # driver.international_hotel()
    # sleep(2)
    driver = MainRoutes()
    driver.train()
    sleep(2)
    # driver = MainRoutes()
    # driver.insurance()
    # sleep(2)