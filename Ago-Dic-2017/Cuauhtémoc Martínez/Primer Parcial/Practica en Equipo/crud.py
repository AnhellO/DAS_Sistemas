from sqlalchemy import create_engine, text, delete
from sqlalchemy.sql import *
from test import Band, Discography, Member


engine = create_engine('sqlite:///sb.db')

def selectFromBand(name):
    conn = engine.connect()
    if name == "":
        s = text("SELECT * FROM Band")
        result =  conn.execute(s)
        for row in result:
            print("\nName: {0}\t\tId: {9}\nCountry: {1}\nLocation: {2}\nStatus: {3}\nFormed In: {4}\nYears Active: {5}\nGenre: {6}\nLyrical Themes: {7}\nLabel: {8}".format(row['name'],
                        row['country'], row['location'], row['status'], row['formed_in'], row['years_active'], row['genre'], row['lyrical_themes'], row['label'], row['id']))
        result.close()
    else:
        s = text("SELECT * FROM Band WHERE Band.name == :x")
        s = s.bindparams(x = name)
        result = conn.execute(s)
        for row in result:
            print("\nName: {0}\t\tId: {9}\nCountry: {1}\nLocation: {2}\nStatus: {3}\nFormed In: {4}\nYears Active: {5}\nGenre: {6}\nLyrical Themes: {7}\nLabel: {8}".format(row['name'],
                        row['country'], row['location'], row['status'], row['formed_in'], row['years_active'], row['genre'], row['lyrical_themes'], row['label'], row['id']))
        result.close()


def selectFromDiscography(name):
    print('\n'*25)
    conn = engine.connect()
    if name == "":
        s = text("SELECT d.name Name, d.release_type Release_Type, d.year Year, b.name Band FROM discography d JOIN band b ON d.band_id = b.id")
        result =  conn.execute(s)
        for row in result:
            print("\nName: {0}\nRelease Type: {1}\nYear: {2}\nBand: {3}".format(row['Name'],
                            row['Release_Type'], row['Year'], row['Band']))
        result.close()
    else:
        s = text("SELECT * FROM Discography WHERE band_id IN (SELECT id FROM Band WHERE name = :x)")
        s = s.bindparams(x = name)
        result = conn.execute(s)
        print("BAND: {0}".format(name))
        for row in result:
            print("\nName: {0}\nRelease Type: {1}\nYear: {2}".format(row['name'],
                        row['release_type'], row['year']))
        result.close()

def selectFromMember(name):
    print('\n'*25)
    conn = engine.connect()
    if name == "":
        s = text("SELECT m.name Name, b.name Band FROM Member m JOIN Band b ON m.band_id = b.id")
        result =  conn.execute(s)
        for row in result:
            print("\nName: {0}\nBand: {1}".format(row['Name'], row['Band']))
        result.close()
    else:
        s = text("SELECT * FROM Member WHERE band_id IN (SELECT id FROM Band WHERE name = :x)")
        s = s.bindparams(x = name)
        result = conn.execute(s)
        print("BAND: {0}".format(name))
        for row in result:
            print("\n{0}".format(row['name']))
        result.close()


def deleteFromMember(name):
    conn = engine.connect()
    s = text("DELETE FROM Member WHERE band_id IN (SELECT id FROM Band WHERE name = :x)")
    s = s.bindparams(x = name)
    result = conn.execute(s)

def deleteFromDiscography(name):
    conn = engine.connect()
    s = text("DELETE FROM Discography WHERE band_id IN (SELECT id FROM Band WHERE name = :x)")
    s = s.bindparams(x = name)
    result = conn.execute(s)

def deleteFromBand(name):
    conn = engine.connect()
    s = text("DELETE FROM Band WHERE name = :x")
    s = s.bindparams(x = name)
    result = conn.execute(s)


def updateMemberName(Oname, Nname):
    conn = engine.connect()
    s = text("UPDATE Member set name = :x WHERE name = :y")
    s = s.bindparams(x = Nname, y = Oname)
    result = conn.execute(s)

def updateDiscographyName(Oname, Nname):
    conn = engine.connect()
    s = text("UPDATE Discography set name = :x WHERE name = :y")
    s = s.bindparams(x = Nname, y = Oname)
    result = conn.execute(s)

def updateBandName(Oname, Nname):
    conn = engine.connect()
    s = text("UPDATE Band set name = :x WHERE name = :y")
    s = s.bindparams(x = Nname, y = Oname)
    result = conn.execute(s)

if __name__ == '__main__':
    selectFromBand()
    #selectFromDiscography()
    #selectFromMember("(Jhator)")
    #deleteFromMember("(Jhator)")
    #deleteFromDiscography("(Jhator)")
    #deleteFromBand("(Jhator)")

    #updateMemberName("Ola Berg","New Name")
    #updateDiscographyName("Morte", "New Name")
    #updateBandName("- - -", "New Name")
