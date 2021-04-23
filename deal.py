class BaseDeal:
    def __init__(self, client_name, seller_name, date, **kwargs):
        super().__init__(**kwargs)
        self.client_name = client_name
        self.seller_name = seller_name
        self.date = date

    @classmethod
    def prompt(cls):
        client_name = input('Please enter client name:')
        seller_name = input('Please enter seller name:')
        date = input('Please enter date:')

        result = {
            'client_name': client_name,
            'seller_name': seller_name,
            'date': date
        }

        return result


class RentDeal(BaseDeal):
    def __init__(self, pre_paid, monthly_cost, **kwargs):
        super().__init__(**kwargs)
        self.pre_paid = pre_paid
        self.monthly_cost = monthly_cost

    @classmethod
    def prompt(cls):
        pre_paid = input('Please enter pre paid amount:')
        monthly_cost = input('Please enter monthly cost:')

        result = {
            'pre_paid': pre_paid,
            'monthly_cost': monthly_cost
        }
        result.update(BaseDeal.prompt())

        return result


class PurchaseDeal(BaseDeal):
    def __init__(self, total_cost, **kwargs):
        super().__init__(**kwargs)
        self.total_cost = total_cost

    @classmethod
    def prompt(cls):
        total_cost = input('Please enter total cost amount:')

        result = {
            'total_cost': total_cost
        }
        result.update(BaseDeal.prompt())

        return result
