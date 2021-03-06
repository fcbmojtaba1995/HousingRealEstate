from constants import PROFILE_MAPPER, PROFILES_FILE_PATH
from decorators import check_access
from deal import RentDeal, PurchaseDeal
from store import load_data

class BaseUser:
    def __init__(self, username, password, first_name, last_name, email, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @classmethod
    def prompt(cls):
        username = input('Please enter your username:')
        password = input('Please enter your password:')
        first_name = input('Please enter your first_name:')
        last_name = input('Please enter your last_name:')
        email = input('Please enter your email:')

        result = {
            'username': username,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }

        return result


class Supervisor(BaseUser):
    agents_list = list()
    properties_list = dict()
    deals_list = list()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def create_agent():
        agent_data = Agent.prompt()
        agent = Agent(**agent_data)
        return agent

    @classmethod
    def agent_data(cls):
        tmp = list()
        for agent in cls.agents_list:
            tmp.append(agent.serializer())
        return tmp

    @classmethod
    def search_username(cls, username):
        for agent in cls.agents_list:
            if agent.username == username:
                return agent
        return None


class Agent(BaseUser):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Supervisor.agents_list.append(self)
        self.__has_access = False
        self.properties_list = list()
        self.deals_list = list()

    @classmethod
    def prompt(cls):
        return BaseUser.prompt()

    def serializer(self):
        data = self.__dict__
        data.pop('properties_list')
        data.pop('deals_list')
        data.pop('_Agent__has_access')
        return data

    def check_password(self, password):
        check = self.password == password
        if check:
            self.__has_access = True
        return check

    def has_access(self):
        return self.__has_access

    @staticmethod
    @check_access
    def add_profile(obj):
        house_or_apartment = input('Please choose house or apartment?')
        rent_or_purchase = input('Please choose rent or purchase?')
        input_tuple = (house_or_apartment, rent_or_purchase)
        profile_class = PROFILE_MAPPER[input_tuple]
        return input_tuple, profile_class.prompt()

    @staticmethod
    @check_access
    def add_deal(obj):
        rent_or_purchase = input('Please choose rent or purchase?')
        if rent_or_purchase == 'rent':
            return RentDeal.prompt()
        elif rent_or_purchase == 'purchase':
            return PurchaseDeal.prompt()

    @staticmethod
    def search():
        return load_data(PROFILES_FILE_PATH)
