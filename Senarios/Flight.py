from helium import *
from base import Base
from Modules.search import Search
from Modules.result import Result
from Modules.revalidate import revalidate
from Modules.profile import Profile
from time import sleep

class Flight(Base):

    class DomesticOnewayFlightBooking:

        def domestic_flight_booking_with_passenger_data_entry(self):
            Search().Flight("domestic", "oneway")
            sleep(15)
            Result().FlightResult().result()
            sleep(3)
            revalidate().Domestic_Flight("new_passenger")
            sleep(3)
            kill_browser()


        def domestic_flight_booking_with_logged_in_user(self):
            '''

            '''
            Profile().Login().login()
            Search().Flight("domestic", "oneway")
            sleep(15)
            Result().FlightResult().result()
            revalidate().Domestic_Flight("new_passenger")
            sleep(5)
            kill_browser()

        def domestic_flight_booking_using_passenger_booklet(self):
            Search().Flight("domestic", "oneway")
            # wait_until(Button("جزئیات و خرید").exists())
            # wait_until(lambda: not Text("در حال جستجوی بهترین پرواز ها").exists())
            sleep(15)
            Result().FlightResult().result()
            sleep(3)
            revalidate().Domestic_Flight("from_booklet")
            sleep(5)
            kill_browser()



    class DomesticRoundTripFlightBooking:

        def domestic_round_trip(self):
            Profile().Login().login()
            Search().Flight("domestic", "roundTrip")
            sleep(15)
            Result().FlightResult().result()
            revalidate().Domestic_Flight("new_passenger")
            sleep(2)
            kill_browser()



    class InternationalOnewayFlightBooking:

        def international_oneway(self):
            Profile().Login().login()
            Search().Flight("international", "oneway")
            sleep(15)
            Result().FlightResult().result()
            revalidate().international_flight()
            sleep(2)
            kill_browser()




    class InternationalRoundTripFlightBooking:

        def international_round_trip(self):
            Profile().Login().login()
            Search().Flight("international", "roundTrip")
            sleep(15)
            Result().FlightResult().result()
            revalidate().international_flight()
            sleep(2)
            kill_browser()






if __name__ == "__main__":
    # driver = Flight().DomesticOnewayFlightBooking()
    # driver.domestic_flight_booking_with_passenger_data_entry()
    # sleep(2)
    # driver = Flight().DomesticOnewayFlightBooking()
    # driver.domestic_flight_booking_with_logged_in_user()
    # sleep(2)
    # driver = Flight().DomesticOnewayFlightBooking()
    # driver.domestic_flight_booking_using_passenger_booklet()
    # sleep(2)
    # driver = Flight().DomesticRoundTripFlightBooking()
    # driver.domestic_round_trip()
    # sleep(2)
    # driver = Flight().InternationalOnewayFlightBooking()
    # driver.international_oneway()
    # sleep(2)
    driver = Flight().InternationalRoundTripFlightBooking()
    driver.international_round_trip()
