filters = {
	'Domestic Filters' :
		{
			'12LPH' : [219, 220, 221, 222, 223, 224, 225, 226, 227, 228,
			238, 239, 240, 241, 242, 243, 244, 547, 553],

			'25LPH' : [212, 213, 214],

			'40LPH' : [215],

			'50LPH' : [216, 217, 218]
		},


	'Industrial Filters' :

		{
			'100LPH' : [486],

			'250LPH' : [487,490],

			'500LPH' : [495,498,500],

			'1000LPH' : [511,515,517],

			'2000LPH' : [539, 540],

			'3000LPH' : [543]
		}
}


# filters = {
# 	'Domestic Filters' : {
# 		'25LPH' : [212, 213],

# 		'40LPH' : [215]
# 	},
# 	'Industrial Filters' :{
# 		'100LPH' : [486],

# 		'250LPH' : [487,490]
# 	}
# }

	
# for _filter in filters:
# 	print(_filter)
# 	for x,y in filters[_filter].items():
# 		print(x)
# 		for z in y:
# 			print(z)

# import json

# with open('filter_data.json', 'r') as file:
# 	a = json.load(file)
	
# b = a['Domestic Filters']['25LPH']

# for i in b:
# 	print(b[i])
# 	print('\n')