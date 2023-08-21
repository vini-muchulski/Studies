# Track Location using IP Address with Python | Location Tracking using Python
import geocoder
import folium   

g = geocoder.ip("me")

print(g)
x = g.latlng
print(x[0], x[1])

my_map1 = folium.Map(location = [x[0], x[1]],
                                        zoom_start = 12 )

folium.CircleMarker(location = [28.5011226, 77.4099794],radius = 50, popup = ' FRI ').add_to(my_map1)

print(my_map1)