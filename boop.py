from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def calc_launch_distance():
  geolocator = Nominatim(user_agent="Nuclear Missile Lauch")

  launch_city_loc = geolocator.geocode('New York City')

  new_york = (launch_city_loc.latitude, launch_city_loc.longitude)


  target_city = input('Enter target city: ')

  target_city_loc = geolocator.geocode(f'{target_city}')

  target_city_coor = (target_city_loc.latitude, target_city_loc.longitude)

  launch_distance = geodesic(new_york, target_city_coor).miles

  return launch_distance
  
print(calc_launch_distance())

