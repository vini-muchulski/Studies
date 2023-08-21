import phonenumbers

from teste import numero

from phonenumbers import geocoder
from phonenumbers import carrier

#Python Project | Track Phone Number Location Using Python

ch_number = phonenumbers.parse(numero,"CH")

print(geocoder.description_for_number(ch_number,"en"))

service_number = phonenumbers.parse(numero,"RO")
print(carrier.name_for_number(service_number,"en"))