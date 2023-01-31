# import datetime
#
#
# class Forest:
#     _life_is_like_a_box_of: str = 'chocolate'
#
#     def __init__(self, last_name: str, shrimp_company: str, state: str, bdate: datetime.date,
#                  hair_style: str = 'karahat'):
#         self._last_name: str = last_name
#         self._shrimp_company: str = shrimp_company
#         self._state: str = state
#         self._birth_date: datetime.date = bdate
#         self._hair_style: str = hair_style
#         self._actor: str = 'tom_hanks'
#         self._life = Forest._life_is_like_a_box_of
#
#     def get_birth_date(self) -> datetime.date:
#         return self._birth_date
#
#     def get_last_name(self):
#         return self._last_name
#
#     def get_age(self):
#         return datetime.date.today().year - self._birth_date.year
#
#     def __str__(self):
#         return f"{self._last_name} {self._shrimp_company} {self._state}"
#
# #   @property
# #   def life_is_like_a_box_of(self):
# #       return self._life_is_like_a_box_of
#
#
# if __name__ == '__main__':
#     tom = Forest('Gump', 'BuBu_Gunp', 'Alabama', datetime.date(1963, 7, 2))
#     print(tom.get_age())
#     print(tom._life_is_like_a_box_of)
#     print(tom)

import First_Class.class Forest
