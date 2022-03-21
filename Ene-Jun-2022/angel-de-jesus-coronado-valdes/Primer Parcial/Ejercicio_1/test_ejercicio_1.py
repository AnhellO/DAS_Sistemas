import pytest
from ejercicio_1 import *


page = [
    [
        Page("https://www.angel.com/init","init","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> my first page web </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> en el rio-arcadia libre.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'my.png'>"),
        Page("https://www.angel.com/logi","logi","<a href= 'https://www.facebook.com' target='_blank'> FACEBOOK </a>","<p> this is facebook </p>","<h3> hello </h3>","<p> html </p>","<p> my web site </p>","<audio> hello.mp3 </audio>","<video> hello.mp4 </video>","<img src='hoooo.png'>"),
        Page("https://www.angel.com/menu","menu","<a href= 'https://www.yahoo.com' target='_blank'> YAHOO </a>","<p> this is yahoo </p>","<h3> poom </h3>","<p> html </p>","<p> my web site </p>","<audio> nana pancha.mp3 </audio>","<video> my friends.mp4 </video>","<img src= 'hellsing.png'>"),
        Page("https://www.angel.com/catalog","catalogo","<a href= 'https://www.twitter.com' target='_blank'> TWTTER </a>","<p> this is twitter </p>","<h3> arcadia libre </h3>","<p> html </p>","<p> my web site </p>","<audio> menos yo-sekta core.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'onepuchman.png'>"),
        Page("https://www.angel.com/maps","maps","<a href= 'https://www.python.com' target='_blank'> PYTHON </a>","<p> this is python </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> experts.mp3 </audio>","<video> parkour.mp4 </video>","<img src= 'my.png'>"),
    ],
    [
        Page("https://www.spiders.com/initspider","initspider","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> page web </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> sound.mp3 </audio>","<video> my spiderworld.mp4 </video>","<img src= 'Lycosidae.png'>"),
        Page("https://www.spiders.com/logispider","logispider","<a href= 'https://www.facebook.com' target='_blank'> FACEBOOK </a>","<p> this is facebook </p>","<h3> Json </h3>","<p> javaScript </p>","<p> web site </p>","<audio> mysound.mp3 </audio>","<video> documents.mp4 </video>","<img src= 'salticidae.png'>"),
        Page("https://www.spiders.com/menuspider","menuspider","<a href= 'https://www.yahoo.com' target='_blank'> YAHOO </a>","<p> this is yahoo </p>","<h3> poom </h3>","<p> php </p>","<p> spider menu </p>","<audio> description.mp3 </audio>","<video> expert.mp4 </video>","<img src= 'salticidaess66.png'>"),
        Page("https://www.spiders.com/catalogospider","catalogospider","<a href= 'https://www.twitter.com' target='_blank'> TWITTER </a>","<p> this is twitter </p>","<h3> catalogue </h3>","<p> xml </p>","<audio> cantalogue of spider </p>","the world.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'one.png'>"),
        Page("https://www.spiders.com/mapspider","mapspider","<a href= 'https://www.spidersmuch.com' target='_blank'> SPIDERSMUCH </a>","<p> this is spidersmuch </p>","<h3> spidersmuch it is the best page of spiders </h3>","<p> php </p>","<p> description </p>","<audio> helloworld.mp3 </audio>","<video> spidersmuch.mp4 </video>","<img src= 'spidersmuch33.png'>"),
    ],
    [
        Page("https://www.ghots.com/initghots","initghots","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> this is video of ghots </p>","<h3> ghots world </h3>","<p> php </p>","<p> page of ghots </p>","<audio> soundghots.mp3 </audio>","<video> evidents.mp4 </video>","<img src= 'ghost_in_my_house.png'>"),
        Page("https://www.ghots.com/logighots","logighots","<a href= 'https://www.facebook.com' target='_blank'> FACEBOOK </a>","<p> this is we facebook page </p>","<h3> ghotsland </h3>","<p> php </p>","<p> page of images </p>","<audio> sound2.mp3 </audio>","<video> ghots.mp4 </video>","<img src= 'graveyard.png'>"),
        Page("https://www.ghots.com/menughots","menughots","<a href= 'https://www.yahoo.com' target='_blank'> YAHOO </a>","<p> this is yahoo </p>","<h3> description my web page </h3>","<p> php </p>","<p> my web site of ghots </p>","<audio> booh.mp3 </audio>","<video> ghots_in_graveyard.mp4 </video>","<img src= 'evil.png'>"),
        Page("https://www.ghots.com/catalogoghots","catalogoghots","<a href= 'https://www.twitter.com' target='_blank'> TWITTER </a>","<p> this is twitter </p>","<h3> animals </h3>","<p> php </p>","<p> ghots and animal </p>","<audio> animals.mp3 </audio>","<video> dogs.mp4 </video>","<img src= 'dog_with_ghots.png'>"),
        Page("https://www.ghots.com/mapsghots","mapsghots","<a href= 'https://www.ghotsll33.com' target='_blank'> GHOTSLL33 </a>","<p> this is ghotsll33 </p>","<h3> ghotsll33 </h3>","<p> php </p>","<p> my web site ghotsll33 </p>","<audio> ghotsll33.mp3 </audio>","<video> ghotsll33.mp4 </video>","<img src= 'ghotsll33.png'>"),
    ]
]
website = [
    Website("https://www.angel.com",page[0],"angel","my option","wechat","catalogue of work","yourmaps"),
    Website("https://www.spiders.com",page[1],"the spiders","spiders of world","spider-chat","catalogue of spiders","spiders-maps"),
    Website("https://www.ghots.com",page[2],"ghots","ghots","ghots-chat","catalogue of ghots","ghots-maps")
]

@pytest.mark.parametrize("items,expected",[
    (
        str(Seeker(website, page, "https://www.angel.com","init").seekerweb()),
        "My Web Site is\nDOMAIN: https://www.angel.com\n\n[ PAGE WEB ]\nURL: https://www.angel.com/init\nNAME: init\nHYPERLINKS: <a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>\nTEXT: <p> my first page web </p>\nTITLE: <h3> world </h3>\nFORMAT: <p> html </p>\nMETADESCRIPTION: <p> my web site </p>\nSOUND: <audio> en el rio-arcadia libre.mp3 </audio>\nVIDEO: <video> hello.mp4 </video>\nIMAGE: <img src= 'my.png'>\n\nADMIN: angel\nMENU: my option\nCHAT: wechat\nCATALOGUE: catalogue of work\nMAPA: yourmaps"
    ),
    (
        str(Seeker(website, page, "https://www.angel.com","initio").seekerweb()),
        "PAGE NOT FOUND"
    ),
    (
        str(Seeker(website, page, "https://www.juan.com","init").seekerweb()),
        "SITE NOT FOUND"
    ),
])

def test_seeker(items,expected):
    assert items == expected

def test_page():
    page = Page("https://www.angel.com/init","init","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> my first page web </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> en el rio-arcadia libre.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'my.png'>")
    result = "\nURL: https://www.angel.com/init\nNAME: init\nHYPERLINKS: <a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>\nTEXT: <p> my first page web </p>\nTITLE: <h3> world </h3>\nFORMAT: <p> html </p>\nMETADESCRIPTION: <p> my web site </p>\nSOUND: <audio> en el rio-arcadia libre.mp3 </audio>\nVIDEO: <video> hello.mp4 </video>\nIMAGE: <img src= 'my.png'>\n"
    assert str(page) == result

def test_web_site():
    page = Page("https://www.angel.com/init","init","<a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>","<p> my first page web </p>","<h3> world </h3>","<p> html </p>","<p> my web site </p>","<audio> en el rio-arcadia libre.mp3 </audio>","<video> hello.mp4 </video>","<img src= 'my.png'>")
    web = Website("https://www.angel.com",page,"angel","my option","wechat","catalogue of work","yourmaps")
    result = "My Web Site is\nDOMAIN: https://www.angel.com\n\n[ PAGE WEB ]\nURL: https://www.angel.com/init\nNAME: init\nHYPERLINKS: <a href= 'https://www.youtube.com' target='_blank'> YOUTUBE </a>\nTEXT: <p> my first page web </p>\nTITLE: <h3> world </h3>\nFORMAT: <p> html </p>\nMETADESCRIPTION: <p> my web site </p>\nSOUND: <audio> en el rio-arcadia libre.mp3 </audio>\nVIDEO: <video> hello.mp4 </video>\nIMAGE: <img src= 'my.png'>\n\nADMIN: angel\nMENU: my option\nCHAT: wechat\nCATALOGUE: catalogue of work\nMAPA: yourmaps"
    web.chosenpage = page
    assert str(web) == result




