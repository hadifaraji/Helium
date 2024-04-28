from helium import *
from time import sleep
from Modules.profile import Profile


class revalidate:
    def domestic_flight(self):
        write("Mohammad", into="نام لاتین")
        write("Afraz", into="نام خانوادگی لاتین")
        click("تاریخ تولد")
        sleep(1)
        click("روز")
        press(NUMPAD3)
        sleep(2)
        click("ماه")
        press(NUMPAD3)
        sleep(2)
        click("سال")
        press(NUMPAD1 + NUMPAD3 + NUMPAD7 + NUMPAD3)
        sleep(1)
        click("ثبت")
        write("0017678129", into="کد ملی")
        click("ادامه فرآیند خرید")
        # click("ادامه فرآیند خرید")
        sleep(3)
        click("اینجانب")
        click("ادامه فرآیند خرید")


    def Domestic_Flight(self, passenger=None):
        if passenger == "from_booklet":
            Profile().Passengers().passenger_booklet()
        elif passenger == "new_passenger":
            write("Melika", into="نام لاتین")
            write("Farahani", into="نام خانوادگی لاتین")
            click("تاریخ تولد")
            sleep(1)
            click("روز")
            press(NUMPAD1 + NUMPAD9)
            sleep(2)
            click("ماه")
            press(NUMPAD4)
            sleep(2)
            click("سال")
            press(NUMPAD1 + NUMPAD3 + NUMPAD8 + NUMPAD5)
            sleep(1)
            click("ثبت")
            write("0200801023", into="کد ملی")
            click("ادامه فرآیند خرید")
            sleep(3)
            if Text("اینجانب").exists():
                click("اینجانب")
                click("ادامه فرآیند خرید")
                sleep(2)
            else:
                Profile().Login.login(self)
                sleep(4)
                click("ادامه فرآیند خرید")
                click("اینجانب")
                click("ادامه فرآیند خرید")
                sleep(2)


    def international_flight(self):
        write("Mohammad", into="نام لاتین")
        write("Afraz", into="نام خانوادگی لاتین")
        click("تاریخ تولد")
        sleep(1)
        click("روز")
        press(NUMPAD3)
        sleep(2)
        click("ماه")
        press(NUMPAD3)
        sleep(2)
        click("سال")
        press(NUMPAD1 + NUMPAD3 + NUMPAD7 + NUMPAD3)
        sleep(1)
        click("ثبت")
        write("A12345678", into="شماره پاسپورت")
        click("تاریخ انقضای پاسپورت")
        sleep(1)
        click("روز")
        press(NUMPAD3)
        sleep(2)
        click("ماه")
        press(NUMPAD3)
        sleep(2)
        click("سال")
        press(NUMPAD1 + NUMPAD4 + NUMPAD1 + NUMPAD1)
        sleep(1)
        click("ثبت")
        write("0017678129", into="کد ملی")
        click("ادامه فرآیند خرید")
        # click("ادامه فرآیند خرید")
        sleep(3)
        click("اینجانب")
        click("ادامه فرآیند خرید")

    def domestic_hotel(self, name="محمد", surename="افراز", national_code="0017678129"):
        scroll_down(300)
        sleep(3)
        # write(name, into="نام")
        first_name=find_all(TextField("نام"))
        write(name, into=first_name[1])
        sleep(2)
        write(surename, into="نام خانوادگی")
        sleep(2)
        write(national_code,into="کد ملی")
        sleep(2)
        click("جنسیت")
        click("مرد")


    def international_hotel(self, latin_name="Mohammad", latin_surename="Afraz"):
        scroll_down(100)
        write(latin_name, into="نام(لاتین)")
        write(latin_surename, into="نام خانوادگی(لاتین)")
        click("جنسیت")
        click("مرد")

        sleep(3)

    def train(self):
        write("محمد", into="نام خود را به فارسی وارد کنید")
        write("افراز", into="نام خانوادگی خود را به فارسی وارد کنید")
        click("تاریخ تولد")
        sleep(1)
        click("روز")
        press(NUMPAD3)
        sleep(2)
        click("ماه")
        press(NUMPAD1 + NUMPAD0)
        sleep(2)
        click("سال")
        press(NUMPAD1 + NUMPAD3 + NUMPAD7 + NUMPAD3)
        sleep(1)
        click("ثبت")
        write("0017678129", into="کد ملی")
        write("afrazmhosin@gmail.com", into="ایمیل")
        write("09010202136", into="موبایل")
        if Text("انتخاب کنید").exists():
            click("انتخاب کنید")
            if Text("بدون غذا - رایگان ").exists():
                click("بدون غذا - رایگان ")
            elif Text("بدون هتل و بدون پرداخت هزینه - رایگان").exists():
                click("بدون هتل و بدون پرداخت هزینه - رایگان")
        click("ادامه فرآیند خرید")
        # click("ادامه فرآیند خرید")
        sleep(3)
        click("اینجانب")
        click("ادامه فرآیند خرید")
    def insurance(self):
        write("Mohammad", into="نام لاتین")
        write("Afraz", into="نام خانوادگی لاتین")
        click("تاریخ تولد (میلادی)")
        sleep(1)
        click("Day")
        press(NUMPAD3)
        sleep(2)
        click("Month")
        press(NUMPAD1)
        sleep(2)
        click("Year")
        press(NUMPAD1 + NUMPAD9 + NUMPAD9 + NUMPAD5)
        sleep(1)
        click("ثبت")
        click("انتخاب کنید")
        click("Single")
        write("A12345678", into="شماره پاسپورت")
        write("0017678129", into="کد ملی")

