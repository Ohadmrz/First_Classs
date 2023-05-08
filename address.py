

class Address:
    def __init__(self, block: str, section: int, cell_num: int) -> None:
        self._block: str = block
        self._section: int = section
        self._cell_num: int = cell_num

    def __str__(self):
        return f"  <(x)/X\(x)>   Block: {self._block}\n    </(X)\>     Section: {self._section}   \n      |x|       Cell: {self._cell_num}"


if __name__ == '__main__':
    gh = Address('b', 5, 19)
    print(gh)
