from profile import ApartmentRental, ApartmentPurchasable, HouseRental, HousePurchasable
SUPERVISOR_CREDENTIALS = [
    {'username': 'admin', 'password': '123'},
    {'username': 'admin2', 'password': '1234'},
    {'username': 'admin3', 'password': '12345'}
]
AGENT_FILE_PATH = '../fixtures/agents.json'

PROFILE_MAPPER = {
    ('house', 'rent'): HouseRental,
    ('house', 'purchase'): HousePurchasable,
    ('apartment', 'rent'): ApartmentRental,
    ('apartment', 'purchase'): ApartmentPurchasable
}
