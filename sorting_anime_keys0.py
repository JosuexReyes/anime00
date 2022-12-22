#List of animes I have been recommended 

anime = {'Overlord':52, 'Dororo':24, 'Black Bullet':13, 'One Piece':1026, 'Monster':74, 'Vivy Florite Eyes Song':13, 'Kenshin':95, 'Danmachi':59, 'Log Horizon':25, 'Wonder Egg Priority':12, 'Student Council President Maid':26, 'Grave of Fireflies':1, 'Inazume Eleven':127, 'Komisan':24, 'The Garden of Sinners':13, 'Kaguyasama':37, 'Odd Taxi':13, 'Samurai Champloo':23, 'Moriarty the Patriot':24, 'Evangelion':26, 'Maburaho':24, 'Ya Boy Kongming':12, 'Gintama':367, 'Psychoo Pass':22, 'Saiki k':120, 'Mob Psycho 100':25}
anime.items

sorted(anime.keys())
for key in sorted(anime.keys()):
	print(key, ":", anime[key])
