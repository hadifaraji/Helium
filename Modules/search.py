from helium import *
from time import sleep

class Search:

    def hotel(self, hotel_type, city_hotel_name=None):
        if hotel_type == "domestic":

            click("هتل داخلی")
            city_hotel_name = "تهران"
        elif hotel_type == "international":
            click("هتل خارجی")
            city_hotel_name = "Istanbul"

        click("نام شهر، هتل یا منطقه")
        write(city_hotel_name, into="جستجوی شهر یا هتل")
        click(city_hotel_name)

        click("جستجو")
        sleep(3)

    def flight(self, flight_type, origin=None, destination=None):
        if flight_type == "domestic":
            click("پرواز داخلی")
            origin = "کیش"
            destination = "تهران"
        elif flight_type == "international":
            click("پرواز خارجی")
            origin = "تهران"
            destination = "استانبول"

        click("مبدا")
        write(origin, into="جستجوی مبدا")
        click(origin)

        click("مقصد")
        write(destination, into="جستجوی مقصد")
        click(destination)

        click("جستجو")
        sleep(3)



    def Flight(self, flight_type,ticket_type, origin=None, destination=None):
        if flight_type == "domestic":
            click("پرواز داخلی")
            if ticket_type == "oneway":
                origin = "مشهد"
                destination = "تهران"
            elif ticket_type == "roundTrip":
                click(Button("یک طرفه"))
                click("رفت و برگشت")
                origin = "مشهد"
                destination = "تهران"

        elif flight_type == "international":
            click("پرواز خارجی")
            if ticket_type == "oneway":
                origin = "تهران"
                destination = "استانبول"
            elif ticket_type == "roundTrip":
                click(Button("یک طرفه"))
                click("رفت و برگشت")
                origin = "تهران"
                destination = "استانبول"

        click("مبدا")
        write(origin, into="جستجوی مبدا")
        click(origin)

        click("مقصد")
        write(destination, into="جستجوی مقصد")
        click(destination)

        if ticket_type == "roundTrip":
            click("تاریخ برگشت")
            click("23")
            click("تائید")

        click("جستجو")
        sleep(3)



    def train(self, origin="تهران", destination="شیراز"):
        click("قطار")
        click("مبدا")
        write(origin, into="جستجوی مبدا")
        click(origin)
        click("مقصد")
        write(destination, into="جستجوی مقصد")
        click(destination)
        click("جستجو")
        sleep(3)

    def insurance(self, country_name="ترکیه"):
        click("بیمه مسافرتی")
        click("نام کشور")
        write(country_name,into="نام کشور")
        click(country_name)
        click("مدت سفر")
        click("3 روزه")
        click("جستجو")
        sleep(3)

