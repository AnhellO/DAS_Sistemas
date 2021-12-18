"Facade "
import time
from decimal import Decimal
from game_api import GameAPI

USER = {"user_name": "sean"}
USER_ID = GameAPI.register_user(USER)

time.sleep(1)

GameAPI.submit_entry(USER_ID, Decimal('5'))

time.sleep(1)

print()
print("Gamestate" )
print(GameAPI.game_state())

time.sleep(1)

historial = GameAPI.get_history()

print()
print("Reports History ")
for i in historial:
    print(f"{i} : {historial[i][0]} : {historial[i][1]}")

print()
print("Gamestate ")
print(GameAPI.game_state())