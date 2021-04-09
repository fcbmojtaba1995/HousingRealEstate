class BaseDeal:
    def __init__(self, client_name, seller_name, date, **kwargs):
        super().__init__(**kwargs)
        self.client_name = client_name
        self.seller_name = seller_name
        self.date = date


class RentDeal(BaseDeal):
    def __init__(self, pre_paid, monthly_cost, **kwargs):
        super().__init__(**kwargs)
        self.pre_paid = pre_paid
        self.monthly_cost = monthly_cost


class PurchaseDeal(BaseDeal):
    def __init__(self, total_cost, **kwargs):
        super().__init__(**kwargs)
        self.total_cost = total_cost
