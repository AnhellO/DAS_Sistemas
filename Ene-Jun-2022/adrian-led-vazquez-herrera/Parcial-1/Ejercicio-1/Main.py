#DAS 8vo semestre
#Parcial 1, E: 1 
#Main

from Page_and_website import page, website, search_start

if __name__ == "__main__":

	#We generate the pages
	trex_page=page("Dinowiki - Tyrannosaurus Rex", "www.saurischia.dinowiki.com/trex", "HTML", "T Rex info")
	trex_text= "The most famous dinosaur, the <I>king of tyrant lizards</I>, a carnivorous beast with a height above 3 meters and over 10 meters long"
	trex_page.add_content("Tyrannosaurus Rex", trex_text, "T_rex_reconstruction.jpeg")

	spino_page=page("Dinowiki - Spinosaurus Aegyptiacus", "www.saurischia.dinowiki.com/spino", "HTML", "Spino info")
	spino_text= "The largest theropod dinosaur, a carnivorous semi-aquatic hunter with a height above 4 meters and around 13 meters long"
	spino_page.add_content("Spinosaurus Aegyptiacus", spino_text, "Spino_swimming.jpeg")

	argen_page=page("Dinowiki - Argentinosaurus", "www.saurischia.dinowiki.com/argen", "HTML", "argen info")
	argen_text= "One of the largest dinosaurs, a humongus herbivorous with a shoulder height of 7 meters and a whopping length of 30 meters"
	argen_page.add_content("Argentinosaurus", argen_text, "Argen_group.jpeg")

	#We generate the first subdomain and add the corresponding pages
	saursite=website( "Saurischia dinosaurs website", "dinowiki", "saurischia", "wiki")
	saursite.add(trex_page)
	saursite.add(spino_page)
	saursite.add(argen_page)

	#We generate the pages
	trike_page=page("Dinowiki - Triceratops Horridus", "www.saurischia.dinowiki.com/trike", "HTML", "Trike info")
	trike_text= "A very recognicible face, the <I>three horned face</I>, an herbivorous lizard with a height around 3 meters and between 8 and 9 meters long"
	trike_page.add_content("Triceratops Horridus", trike_text, "grazing_Trike.jpeg")

	paras_page=page("Dinowiki - Parasaurolophus Walkeri", "www.saurischia.dinowiki.com/paras", "HTML", "Paras info")
	paras_text= "The crested and duckbilled dinosaur, an herbivorous grazer with a height on the 5 meters and a length Ankylosaurus magniventrisof 10 meters"
	paras_page.add_content("Parasaurolophus Walkeri", paras_text, "paras_run.jpeg")

	ankyl_page=page("Dinowiki - Ankylosaurus Magniventris", "www.saurischia.dinowiki.com/ankyl", "HTML", "Ankyl info")
	ankyl_text= "The <I>armored lizard with a great belly</I>, a weird looking herbivore with a humble height of 1.7 meters and a length of 6-8 meters"
	ankyl_page.add_content("Ankylosaurus Magniventris", ankyl_text, "ankyl_defense.jpeg")
	
	#We generate the second subdomain and add the corresponding pages
	ornisite=website( "Ornithischia dinosaurs website", "dinowiki", "ornithischia", "wiki")
	ornisite.add(trike_page)
	ornisite.add(paras_page)
	ornisite.add(ankyl_page)

	DinoWeb=website( "Dinosaur website", "dinowiki", "", "wiki")
	DinoWeb.add(saursite)
	DinoWeb.add(ornisite)

	dinowebHP=page( "Dinowiki - Welcome", "www.dinowiki.com", "HTML", "Welcome page")
	DinoWeb.set_homepage(dinowebHP)

	print(DinoWeb.show())

	search_start(DinoWeb, "Dinowiki - Welcome")
	search_start(DinoWeb, "Dinowiki - Tyrannosaurus Rex")


