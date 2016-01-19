__author__ = 'MFlores1'


class Household:
    def __init__(self, household_id):
        # Unique household identifier -> PMCgcID
        self.household_id = household_id
        self.property_id = None
        self.property_name = None
        self.applied_date = None
        # First lease
        # self.lease_begin_date = None
        # self.lease_end_date = None
        # self.move_in_date = None
        # Rent when prospect moves in
        # self.rent_move_in = None
        self.residents = []

    def set_applied_date(self, applied_date):
        self.applied_date = applied_date

class ResidentRecord:
    def __init__(self):
        return
class HeadOfHousehold:
    def __init__(self):
        return





