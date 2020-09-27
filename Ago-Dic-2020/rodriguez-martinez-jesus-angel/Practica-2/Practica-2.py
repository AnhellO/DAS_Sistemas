class Anime():

    def __init__ (self, **kwargs):
        self.__title = kwargs.get('title', '')
        self.__episodes = kwargs.get('episodes', '')
        self.__status = kwargs.get('status', '')
        self.__aired = kwargs.get('aired', '')
        self.__score = kwargs.get('score', '')
        self.__ranked = kwargs.get('ranked', '')
        self.__popularity = kwargs.get('popularity', '')
        self.__english = kwargs.get('english', '')
        self.__synonyms = kwargs.get('synonyms', '')
        self.__japanese = kwargs.get('japanese', '')

    def get_anime_information(self):
        return "Information: \nTitle: {} \nEpisodes: {} \nStatus: {} \nAired: {}\n".format(self.__title, self.__episodes, self.__status, self.__aired)

    def get_anime_statistics(self):
        return "Statistics: \nScore: {} \nRanked: #{} \nPopularity: #{}\n".format(self.__score, self.__ranked, self.__popularity)

    def get_anime_alternative_titles(self):
        return "Alternative Titles: \nEnglish: {} \nSynonysm: {} \nJapanese: {}\n".format(self.__english, self.__synonyms, self.__japanese)


class Character(Anime):

    def __init__ (self, **kwargs):
        super().__init__()
        self.__character_name = kwargs.get('character_name','')
        self.__character_description = kwargs.get('character_description','')
        self.__voice_actor = kwargs.get('voice_actor','')

    def get_character_information(self):
        return "Character name: {}\nCharacter description: {}\n".format(self.__character_name, self.__character_description)

    def set_character_name(self, character_name):
        self.__character_name = character_name

    def get_voice_actor(self):
        return "Voice actor: {}\n".format(self.__voice_actor)

zankyou_no_terror = Anime(title='Zankyou no Terror (VON)', episodes=11, status='Finished Airing', aired='Jul 11, 2014 to Sep 26, 2014', score=8.14, ranked=368, popularity=90, english='Terror in Resonance', synonyms='Terror in Tokyo, Terror of Resonance', japanese='残響のテロル')
print(zankyou_no_terror.get_anime_information())
print(zankyou_no_terror.get_anime_statistics())
print(zankyou_no_terror.get_anime_alternative_titles())

nine = Character(title='Zankyou no Terror (VON)', episodes=11, status='Finished Airing', aired='Jul 11, 2014 to Sep 26, 2014', score=8.14, ranked=368, popularity=90, english='Terror in Resonance', synonyms='Terror in Tokyo, Terror of Resonance', japanese='残響のテロル', character_name='Twelve', character_description='He is a member of sphinx LOL', voice_actor='Sudo Von')
print(nine.get_character_information())
nine.set_character_name('Nine')
print(nine.get_character_information())
