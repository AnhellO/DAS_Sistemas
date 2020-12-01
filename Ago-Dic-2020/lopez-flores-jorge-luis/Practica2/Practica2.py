import pyreserve

class League:
    name=""
    country=""

    #Definir el constructor
    def __init__(self, league_name, league_country):
        self.name = league_name
        self.country = league_country

    def show_name(self):
        print(self.name)

    def show_country(self):
        print(self.country)

class Futbol(League):
    futbolYear = 0
    futbolTeams = ""
    futbolSchedule = 0

    def __init__(self, futbol_name, futbol_country, futbol_year, futbol_teams, futbol_schedule):
        League.__init__(self, futbol_name, futbol_country)
        self.futbolYear = futbol_year
        self.futbolTeams = futbol_teams
        self.futbolSchedule = futbol_schedule

    def get_year(self):
        return self.futbolYear

    def get_teams(self):
        return self.futbolTeams

league1 = League("Premier League", "Inglaterra")

futbol1 = Futbol("Premier League", "Inglaterra", 2020, "Manchester United", "40 Jornadas")
print(futbol1.get_year())
league1.show_country
print(futbol1.get_teams())

pyreverse Practica2/

dot -Tpng classes.dot -o Practica2.png