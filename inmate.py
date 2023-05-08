#import random
import datetime
from address import Address



class Inmate:
    def __init__(self, inmate_id: str, name: str, surname: str, birth_date: datetime.date,
                 address: Address, jail_mail: str, release_date: datetime.date) -> None:
        self._inmate_id: str = inmate_id               #random.randint(10000, 99999)
        self._inmate_name: str = name
        self._inmate_surname: str = surname
        self._birth_date: datetime.date = birth_date
        self._address: Address = address
        self._jmail: str = jail_mail
        self._release_date: datetime.date = release_date

    def get_inmate_id(self) -> str:                                                  # get -  id
        return self._inmate_id

    def get_inmate_name(self) -> str:                                                # get -  name
        return self._inmate_name

    def set_inmate_name(self, new_name: str) -> None:                                # set -  name
        self._inmate_name = new_name.title()

    def get_inmate_surname(self) -> str:                                             # get -  surname
        return self._inmate_surname.title()

    def set_inmate_surname(self, new_surname: str) -> None:                          # set -  surname
        self._inmate_surname = new_surname.title()

    def inmate_fullname(self) -> str:                                                   # fullname #
        return f"{self._inmate_name.title()} {self._inmate_surname.title()}"

    def get_address(self) -> Address:                                                # get -  address
        return self._address

    def set_address(self, new_address: Address) -> None:                             # set -  address
        self._address = new_address

    def get_jmail(self) -> str:                                                      # get -  surname
        return self._jmail

    def set_jmail(self, new_jmail: str) -> None:                                     # get -  surname
        self._jmail = new_jmail

    def get_birth_day(self) -> str:                                                  # get -  birthday
        bday = self._birth_date
        bday_strf = bday.strftime("%d/%m/%Y")
        return bday_strf

    def inmate_age(self) -> str:                                                          # age #
        return f"{datetime.date.today().year - self._birth_date.year} year's old"

    def get_release_date(self) -> str:                                               # get -  release date
        reldate = self._release_date.strftime("%d/%m/%Y")
        relage = self._release_date.year - self._birth_date.year
        agedat = f"{reldate} (at the age of {relage})"
        return agedat

    def set_release_date(self, new_release_date) -> str:                             # set -  release date
        self._release_date = new_release_date
        s_rdate = self._release_date.strftime("%d/%m/%Y")
        return s_rdate

    def __str__(self):
        return f"\033[4;91m\033[100m /|\ Shawshank State Prison /|\ \033[00m\033[98m  \ninmate id:       {self.get_inmate_id()}\nfull name:      {self.inmate_fullname()}\nwas born in:    {self.get_birth_day()} ({self.inmate_age()})\nrelease date:   {self.get_release_date()}\njmail:          {self._jmail}\n_________________________________________\n{self._address}"


if __name__ == '__main__':
    address = Address("B", 12, 245)
    Andy_Dufresne = Inmate('3737', 'Andy', 'Dufresne', datetime.date(1900, 4, 7), address, 'I_Andidnt_do_it@jmail.shw', datetime.date(1966, 7, 11))
    print(Andy_Dufresne)



