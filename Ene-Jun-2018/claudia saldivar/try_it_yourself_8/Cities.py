def describe_city(city, country='chile'):
    msg = city.title() + " esta en " + country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')
