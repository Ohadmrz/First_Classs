
class Address:
    def __init__(self, country, city, street: str, zip_code, building_num, entrance=None, floor=None):
        self._floor = floor
        self._entrance = entrance
        self._building_num = building_num
        self._zip_code = zip_code
        self._street: str = street
        self._city = city
        self._country = country

    def get_city(self):
        return self._city

    def __str__(self):
        return f"<street: {self._street}, city: {self._city}, country: {self._country}>"

    def __repr__(self):
        return f'{self._street}, {self._city}'

#######################################################################################################

class Branch:
    def __init__(self, branch_id: int, name: str, address: Address):
        self._branch_id: int = branch_id
        self._name: str = name
        self._address: Address = address

    def get_branch_id(self):
        return self._branch_id

    def get_branch_name(self):
        return self._name

    def get_branch_address(self) -> Address:
        return self._address

    def set_branch_address(self, new_address: object) -> None:
        self._address = new_address

    def __str__(self):
        return f"<Branch id: {self._branch_id} name: {self._name}>" #{self._address}"

    def __repr__(self):
        return f'\nBranch id- {self._branch_id}  ~  name- {self._name.title()}'


#######################################################################################################
class Customer:
    def __init__(self, customer_id: int, passport_id: int, name: str, surname: str,
                 phone_number: str, address: Address, salary: int) -> None:
        self.__customer_id: int = customer_id
        self.__passport_id: int = passport_id
        self.__name: str = name
        self.__surname: str = surname
        self.__phone_number: str = phone_number
        self.__address: Address = address
        self.__salary: int = salary

    def get_customer_id(self) -> int:
        return self.__customer_id

    def get_customer_passport_id(self) -> int:
        return self.__passport_id

    def get_customer_name(self) -> str:
        return self.__name

    def set_customer_name(self, name: str) -> None:
        self.__name = name

    def get_customer_surname(self) -> str:
        return self.__surname

    def set_customer_surname(self, surname: str) -> None:
        self.__surname = surname

    def get_customer_phone_number(self) -> str:
        return self.__phone_number

    def set_customer_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number

    def get_customer_address(self) -> Address:
        return self.__address

    def set_customer_address(self, address: Address) -> None:
        self.__address = address

    def get_customer_salary(self) -> int:
        return self.__salary

    def set_customer_salary(self, salary: int) -> None:
        self.__salary = salary
#######################################################################################################

class BankAccount:

    def __init__(self, account_id, branch_id):
        self._account_id: int = account_id
        self._branch_id: int = branch_id
        self._balance: float = 0

    def set_branch_id(self, new_branch_id):

        self._branch_id = new_branch_id

    def withdraw(self, amnt: float) -> bool:
        new_balance = self._balance - amnt
        if new_balance >=0:
            self._balance = new_balance
            return True
        else:
            return False

    def deposit(self, amnt: float) -> bool:
        new_balance = self._balance + amnt
        self._balance = new_balance
        return True


    def get_balance(self):
        return self._balance
#######################################################################################################
class Bank:

    def __init__(self, name, address: Address):
        self._name = name
        self._address = address
        self._branches: dict[int, Branch] = {}

        self._customers: dict[int, Customer] = {}
        self._accounts: dict[int, BankAccount] = {}

        self._account2customers: dict[int, set[Customer]] = {}
        self._customer2accounts: dict[int, set[BankAccount]] = {}

    def get_name(self):
        return self._name

    def get_address(self) -> Address:
        return self._address

    def add_branch(self, branch_id: int, name: str,
                   address: Address) -> bool:
        if branch_id in self._branches:
            return False
        branch = Branch(branch_id, name, address)
        self._branches[branch_id] = branch

    def get_branch_by_id(self, branch_id) -> Branch:
        return self._branches.get(branch_id)

    def get_branches_by_city(self, city) -> list[Branch]:
        ret_val = []
        for br_id, branch in self._branches.items():
            if branch.get_branch_address().get_city() == city:
                ret_val.append(branch)    #    _______________________________   _____________________________   _____________________________
        return ret_val           # ret_val = [<Branch id: 300, name: discount>, <Branch id: 414, name: Poalim>, <Branch id: 413, name: Poalim>]

    def update_branch_address(self, branch_id, address: Address) -> bool:
        branch = self._branches.get(branch_id)
        if not branch:
            return False
        branch.set_branch_address(address)
        return True

    def remove_branch_by_id(self, branch_id) -> bool:
        if branch_id in self._branches:
            self._branches.pop(branch_id)
            return True
        else:
            return False

    def create_account(self, account_id, branch_id, customer_ids: set[int]) -> bool:
        """
        Creates a new account and associates it with provided customer ids.
        If customer with provided id does not exist - returns False
        :param account_id: the id of the new account
        :param branch_id: branch id of the new account
        :param customer_ids: ids of the customers that will become holders of this account
        :return:
        """
        if account_id in self._accounts:
            return False

        account_holders = set()
        for customer_id in customer_ids:
            if customer_id not in self._customers:
                return False
            else:
                account_holders.add(self._customers[customer_id])

        account = BankAccount(account_id, branch_id)
        self._accounts[account_id] = account

        self._account2customers[account_id] = account_holders
        for customer_id in customer_ids:
            if customer_id not in self._customer2accounts:
                self._customer2accounts[customer_id] = set()
            self._customer2accounts[customer_id].add(account)
        #print(self._customer2accounts)
        return True

    def add_holder_to_account(self, account_id, customer_id) -> bool:
        if account_id not in self._accounts or customer_id not in self._customers:
            #print(self._customer2accounts)
            return False

        current_account_holders = self._account2customers[account_id]
        new_holder = self._customers[customer_id]
        account = self._accounts[account_id]
        if new_holder in current_account_holders:
            # this person already a holder for this account
            #print(self._customer2accounts)
            return False
        else:
            self._account2customers[account_id].add(new_holder)
            self._customer2accounts[customer_id].add(account)
            #print(self._customer2accounts)
            return True

    def withdraw(self, account_id, amnt) -> bool:
        if account_id not in self._accounts:
            return False
        account = self._accounts[account_id]
        return account.withdraw(amnt)

    def deposit(self, account_id, amnt) -> bool:
        if account_id not in self._accounts:
            return False
        account = self._accounts[account_id]
        return account.deposit(amnt)

    def transfer(self, account_id_from: int, account_id_to: int, amnt) -> bool:
        if account_id_from not in self._accounts or account_id_to not in self._accounts:
            return False

        account_from = self._accounts[account_id_from]
        account_to = self._accounts[account_id_to]

        if account_from.withdraw(amnt):
            account_to.deposit(amnt)
            return True

########################################################################################################
if __name__ == '__main__':

    biranecher = Branch(410, "Poalimski", Address("israel", "tel aviv", "dizingomski", 1212, 4))
    print(f'biranecher::::{biranecher}')

    bank_company = Bank("Didney_conglomorat_Bank",
                    Address("Israel", "Tel Adviv", "Allenby", 12345, 36))

    bank_company.add_branch(300, "discount",
                    Address("Israel", "Tel Aviv", "Dizengoff", 14544, 4))
    bank_company.add_branch(414, "Poalim",
                    Address("Israel", "Tel Aviv", "Hamasger", 67605, 54))
    bank_company.add_branch(410, "Poalim",
                    Address("Israel", "Shoham", "Emek Ayalon", 56798, 2))
    bank_company.add_branch(413, "Poalim",
                    Address("Israel", "Tel Aviv", "Allenby", 13335, 76))


    print(f'_branches:{bank_company._branches}')                 #_branches: {300: <Branch id: 300, name: discount>, 414: <Branch id: 414, name: Poalim>, 410: <Branch id: 410, name: Poalim>, 413: <branch id: 413, name: Poalim>}
    branches = bank_company.get_branches_by_city("Tel Aviv")     # branch_by_city: [<Branch id: 300, name: discount>, <Branch id: 414, name: Poalim>, <Branch id: 413, name: Poalim>]
    print(f'get branch by city:{branches}')                      # br: <Branch id: 300, name: discount>
    for br in branches:                                          # br: <Branch id: 414, name: Poalim>
        if br.get_branch_name() == "Poalim":
            bank_company.update_branch_address(br.get_branch_id(),Address("Israel","Netanya","Tom Lantos",12345,9))
                       # update_branch_address(self,  branch_id  ,address: Address)


    account = BankAccount(55667789, 410)
    customer = Customer(308453422, 2082668, "John", "Ham", "0504680024", Address("Israel", "Shoham", "Tom Lantos", 12345, 9), 9500)
    bank_company.create_account(55667789,410,{308453422})
    bank_company.add_holder_to_account(55667789, 308453422)



