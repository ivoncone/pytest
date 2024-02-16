garden = True
garder_area = 0
garden_orientation = ''

def onchange_garden(garden):
        if garden:
            garden_area = 10.0
            garden_orientation = 'north'
            print(garden_area)
            print(garden_orientation)
        else:
            garden_area = 0.0
            garden_orientation = False
            print(garden_orientation)
            print(garden_area)

print(onchange_garden(garden))