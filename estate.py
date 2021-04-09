class BaseProperty:
    def __init__(self, area, room_numbers, parking, address, **kwargs):
        super().__init__(**kwargs)
        self.area = area
        self.room_numbers = room_numbers
        self.parking = parking
        self.address = address

    @classmethod
    def prompt(cls):
        area = input('Please enter area:')
        room_numbers = input('Please enter room numbers:')
        parking = input('Please specify that has parking or not:')
        address = input('Please select location:')

        result = {
            'area': area,
            'room_numbers': room_numbers,
            'parking': parking,
            'address': address
        }

        return result


class Apartment(BaseProperty):
    def __init__(self, floor, elevator, balcony, **kwargs):
        super().__init__(**kwargs)
        self.floor = floor
        self.elevator = elevator
        self.balcony = balcony

    @classmethod
    def prompt(cls):
        floor = input('Which floor?')
        elevator = input('Has elevator or not?')
        balcony = input('Has balcony or not?')

        result = {
            'floor': floor,
            'elevator': elevator,
            'balcony': balcony
        }
        result.update(BaseProperty.prompt())
        return result


class House(BaseProperty):
    def __init__(self, yard, pool, **kwargs):
        super().__init__(**kwargs)
        self.yard = yard
        self.pool = pool

    @classmethod
    def prompt(cls):
        yard = input('Has yard or not?')
        pool = input('Has pool or not?')

        result = {
            'yard': yard,
            'pool': pool
        }
        result.update(BaseProperty.prompt())
        return result


class Rental:
    def __init__(self, pre_paid, monthly, **kwargs):
        super().__init__(**kwargs)
        self.pre_paid = pre_paid
        self.monthly = monthly

    @classmethod
    def prompt(cls):
        pre_paid = input('Please enter pre paid amount:')
        monthly = input('Please enter monthly amount:')

        result = {
            'pre_paid': pre_paid,
            'monthly': monthly
        }
        return result


class Purchasable:
    def __init__(self, cost, **kwargs):
        super().__init__(**kwargs)
        self.cost = cost

    @classmethod
    def prompt(cls):
        cost = input('Please enter cost:')

        result = {
            'pre_paid': cost
        }
        return result
