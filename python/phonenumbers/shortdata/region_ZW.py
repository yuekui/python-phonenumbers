"""Auto-generated file, do not edit by hand. ZW metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZW = PhoneMetadata(id='ZW', country_code=None, international_prefix=None,
    general_desc=PhoneNumberDesc(national_number_pattern='[139]\\d{2,4}', possible_length=(3, 5)),
    toll_free=PhoneNumberDesc(national_number_pattern='9(?:5[023]|61)', example_number='961', possible_length=(3,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='3\\d{4}', example_number='30123', possible_length=(5,)),
    emergency=PhoneNumberDesc(national_number_pattern='(?:112|99[3-59])', example_number='999', possible_length=(3,)),
    short_code=PhoneNumberDesc(national_number_pattern='11[2469]|3\\d{4}|9(?:5[023]|6[0-25]|9[3-59])', example_number='999', possible_length=(3, 5)),
    carrier_specific=PhoneNumberDesc(national_number_pattern='(?:114|9(?:5[023]|6[0-25]))', example_number='114', possible_length=(3,)),
    short_data=True)
