stuff = ['name', 'map_url', 'img_url', 'location',
         'has_sockets', 'has_wifi', 'has_toilet',
         'can_take_calls', 'seats', 'coffee_price']

for thing in stuff:
    print(f"new_cafe.{thing} = form.{thing}.data")
