from flask import render_template

from route_helper import simple_route
from flask import request
from flask import jsonify

GAME_HEADER = """
<h1>So you can't stop thinking about Harry Potter...</h1>
<p>At any time you can <a href='/reset/'>reset</a> your game.</p>
"""


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return render_template("index.html")



@simple_route('/goto/<where>/')
def open_door(world: dict, where: str) -> str:
    if where == "entrance":
        return "Congratulations! You're free!"
    elif where == "sorting_hat":
        return render_template("sorting_ceremony.html")

@simple_route('/save/house/')
def disclosing_reasons(world:dict, chosen_name:str):
    return render_template("reasons_to_disclose.html")


@simple_route('/disclosing/results/')
def save_results(world:dict, *args)->str:
    world["reasons_to_disclose"].append(request.values.get("reason1", False))
    world["reasons_to_disclose"].append(request.values.get("reason2", False))
    world["reasons_to_disclose"].append(request.values.get("reason3", False))
    world["reasons_to_disclose"].append(request.values.get("reason4", False))
    return render_template("reasons_response.html", world=world)

