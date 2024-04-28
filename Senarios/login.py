from base import Base
from Modules.profile import Profile
from Modules.search import Search
from Modules.result import Result

from time import sleep
from helium import *


class Login(Base):
    def login_homepage(self):
        Profile().login()
        kill_browser()

    def login_domestic_flight_result_page(self):
        Search().flight(flight_type="domestic")
        Result().FlightResult().result()
        # Profile().login()
        kill_browser()


if __name__ == "__main__":
    driver = Login()
    driver.login_homepage()
    sleep(2)
    driver = Login()
    driver.login_domestic_flight_result_page()


