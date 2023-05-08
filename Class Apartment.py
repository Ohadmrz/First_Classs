
class Apartment:

    def __init___(self, address: dict, gira: dict, rooms: dict,
                  bathroom: dict, kitchen_size: int, balconies: dict = 0 ):
        self._addred: dict[str, str] = {}
        self._gira: dict[str, int] = {}
        self._rooms: dict[int,int] = {}
        self._bathroom: dict[int,int] = {}
        self._kitchen_size: int = kitchen_size
        self._balconies: dict[int,int] =  balconies
        self._total_size: int = rooms + bathroom + kitchen_size + balconies


