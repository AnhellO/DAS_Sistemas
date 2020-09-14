class Anime():

    def __init__ (self, title, episodes, status, aired, score, ranked, popularity, english, synonyms, japanese):
        self.title = title
        self.episodes = episodes
        self.status = status
        self.aired = aired
        self.score = score
        self.ranked = ranked
        self.popularity = popularity
        self.english = english
        self.synonyms = synonyms
        self.japanese = japanese

    def get_anime_information(self):
        return "Information: \nTitle: {} \nEpisodes: {} \nStatus: {} \nAired: {}\n".format(self.title, self.episodes, self.status, self.aired)

    def get_anime_statistics(self):
        return "Statistics: \nScore: {} \nRanked: #{} \nPopularity: #{}\n".format(self.score, self.ranked, self.popularity)

    def get_anime_alternative_titles(self):
        return "Alternative Titles: \nEnglish: {} \nSynonysm: {} \nJapanese: {}\n".format(self.english, self.synonyms, self.japanese)


class Character(Anime):

    def __init__ (self, title, episodes, status, aired, score, ranked, popularity, english, synonyms, japanese, character_name, character_description, voice_actor):
        Anime.__init__(self, title, episodes, status, aired, score, ranked, popularity, english, synonyms, japanese)
        self.character_name = character_name
        self.character_description = character_description
        self.voice_actor = voice_actor

    def get_character_information(self):
        return "Character name: {}\nCharacter description: {}\n".format(self.character_name, self.character_description)

    def set_character_name(self, character_name):
        self.character_name = character_name

    def get_voice_actor(self):
        return "Voice actor: {}\n".format(self.voice_actor)


zankyou_no_terror = Anime('Zankyou no Terror (VON)', 11, 'Finished Airing', 'Jul 11, 2014 to Sep 26, 2014', 8.14, 368, 90, 'Terror in Resonance', 'Terror in Tokyo, Terror of Resonance', '残響のテロル')
print(zankyou_no_terror.get_anime_information())
print(zankyou_no_terror.get_anime_statistics())
print(zankyou_no_terror.get_anime_alternative_titles())

nine = Character('Zankyou no Terror (VON)', 11, 'Finished Airing', 'Jul 11, 2014 to Sep 26, 2014', 8.14, 368, 90, 'Terror in Resonance', 'Terror in Tokyo, Terror of Resonance', '残響のテロル', 'Twelve', 'He is a member of sphinx LOL', 'Sudo Von')
print(nine.get_character_information())
nine.set_character_name('Nine')
print(nine.get_character_information())
