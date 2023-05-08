from datetime import datetime, timedelta
from library.book import Book
from inmate import Inmate


class Loan:

    def __init__(self, inmate_id: int, book_id: int, loan_type: int):
        self._inmate_id: int = inmate_id
        self._book_id: int = book_id
        self._loan_type: int = loan_type

        self._start_loan = datetime.today()
        if loan_type == 1:
            self._end_loan = self._start_loan + timedelta(days=+10)
        elif loan_type == 2:
            self._end_loan = self._start_loan + timedelta(days=+5)
        else:
            self._end_loan = self._start_loan + timedelta(days=+2)

    def get_start_loan(self):
         return self._start_loan.strftime("%d/%m/%y")

    def get_end_loan(self):
         return self._end_loan.strftime("%d/%m/%y")



