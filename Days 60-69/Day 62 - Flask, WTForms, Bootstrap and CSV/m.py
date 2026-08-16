dict = {
'csrf_token': 'Ijc1Y2M3NjkyOGU4MTgzYjMyYWM5YmE0MGY4NWM4YmRmYTgwYWQ3MmYi.aoGehA.ehA6L6RWmvyjk_t0LKsPZaqoxk8', 

'cafe': "Anto's Cafe", 

'cafe_location': 'https://www.google.com/maps/place/Lighthaus/@51.5701279,-0.0392317,19z/data=!3m1!4b1!4m6!3m5!1s0x48761db0ffba586b:0x93a04ceef20365f1!8m2!3d51.5701279!4d-0.0392317!16s%2Fg%2F11c6ttrf0p?entry=ttu&g_ep=EgoyMDI2MDgxMi4wIKXMDSoASAFQAw%3D%3D', 

'opening_time': '8AM', 

'closing_time': '9PM', 

'coffee_rating': '3', 

'wifi_rating': '4', 

'socket_availability': '2', 

'submit': 'Submit'
}
dict.pop('csrf_token')
dict.pop('submit')
data_list = [dict[elem] for elem in dict]
print(data_list)