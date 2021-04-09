from estate import Apartment, House, Rental, Purchasable


class ApartmentRental(Apartment, Rental):
    @classmethod
    def prompt(cls):
        result = Apartment.prompt()
        result.update(Rental.prompt())
        return result


class ApartmentPurchasable(Apartment, Purchasable):
    @classmethod
    def prompt(cls):
        result = Apartment.prompt()
        result.update(Purchasable.prompt())
        return result


class HouseRental(House, Rental):
    @classmethod
    def prompt(cls):
        result = House.prompt()
        result.update(Rental.prompt())
        return result


class HousePurchasable(House, Purchasable):
    @classmethod
    def prompt(cls):
        result = House.prompt()
        result.update(Purchasable.prompt())
        return result
