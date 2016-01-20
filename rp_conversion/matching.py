__author__ = 'MFlores1'


class Household:
    def __init__(self, hh_id):
        # Unique household identifier -> PMCgcID
        self.hh_id = hh_id
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

    def add_resident_head_of_household(self, *args, **kwargs):
        self.residents.append(HeadOfHousehold(self, *args, **kwargs))


class OneSiteRecord:
    def __init__(self, property_id, property_name, household_id, billing_name, traffic_source, lease_id, lease_status,
                 unit_id, unit, applied_date, lease_begin_date, lease_end_date, move_in_date, lease_term,
                 unit_address, unit_city, unit_state, unit_zip, unit_country, sqft, move_out_reason, property_number,
                 resm_id, first_name, last_name, gender, birth_month, birth_year, resident_address, resident_city,
                 resident_state, resident_zip, resident_phone, resident_cell, resident_work, resident_fax,
                 resident_email, occupant, co_signer, guarantor, resident_move_in_date,
                 resident_move_out_date, relationship_code, floor_plan_id, rent_amount):

        self.property_id = property_id
        self.property_name = property_name
        self.household_id = household_id
        self.billing_name = billing_name
        self.traffic_source = traffic_source
        self.lease_id = lease_id
        self.lease_status = lease_status
        self.unit_id = unit_id
        self.unit = unit
        self.applied_date = applied_date
        self.lease_begin_date = lease_begin_date
        self.lease_end_date = lease_end_date
        self.move_in_date = move_in_date
        self.lease_term = lease_term
        self.unit_address = unit_address
        self.unit_city = unit_city
        self.unit_state = unit_state
        self.unit_zip = unit_zip
        self.unit_country = unit_country
        self.sqft = sqft
        self.move_out_reason = move_out_reason
        self.property_number = property_number
        self.resm_id = resm_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.resident_address = resident_address
        self.resident_city = resident_city
        self.resident_state = resident_state
        self.resident_zip = resident_zip
        self.resident_phone = resident_phone
        self.resident_cell = resident_cell
        self.resident_work = resident_work
        self.resident_fax = resident_fax
        self.resident_email = resident_email
        self.occupant = occupant
        self.co_signer = co_signer
        self.guarantor = guarantor
        self.resident_move_in_date = resident_move_in_date
        self.resident_move_out_date = resident_move_out_date
        self.relationship_code = relationship_code
        self.floor_plan_id = floor_plan_id
        self.rent_amount = rent_amount


class HeadOfHousehold (OneSiteRecord):
    def __init__(self, *args, **kwargs):
        # super(HeadOfHousehold, self).__init__(*args, **kwargs)
        OneSiteRecord.__init__(self, *args, **kwargs)

h1 = Household('1')
h1.add_resident_head_of_household('1', 's')
