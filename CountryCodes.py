import phonenumbers
from phonenumbers import geocoder
p1 = phonenumbers.parse("+917794958387")
print(geocoder.description_for_valid_number(p1,"en"))