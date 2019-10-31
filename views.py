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
        return render_template("sorting_ceremony.html", world = world)

@simple_route('/save/house/')
def disclosing_reasons(world:dict, chosen_name:str):
    world["house"]=request.values.get("houses")
    if world["house"]=="Gryffindor":
        return render_template("gryffindor_survey.html", world=world)
    elif world["house"]=="Hufflepuff":
        return render_template("hufflepuff_survey.html", world=world)
    elif world["house"]=="Ravenclaw":
        return render_template("ravenclaw_survey.html", world=world)
    elif world["house"]=="Slytherin":
        return render_template("slytherin_survey.html", world=world)

def calculating_result()->int:
    for reason in reasons:
        total=0
        if reason in reasons[:4]:
            total+=1
            return total
        elif reason in reasons[4:]:
            total-=1
            return total

@simple_route('/disclosing/results/')
def results_subject(world:dict, *args)->str:
    """

    :type world: dict
    """

    world["reasons_to_disclose"].append(request.values.get("reason1", False))
    world["reasons_to_disclose"].append(request.values.get("reason2", False))
    world["reasons_to_disclose"].append(request.values.get("reason3", False))
    world["reasons_to_disclose"].append(request.values.get("reason4", False))
    world["reasons_not_to_disclose"].append(request.values.get("neg1", False))
    world["reasons_not_to_disclose"].append(request.values.get("neg2", False))
    world["reasons_not_to_disclose"].append(request.values.get("neg3", False))
    world["receiving_disclosure"]=request.values.get("person")
    for reason in world["reasons_to_disclose"]:
        if reason != False:
            world["total"]+=1
    for reason in world["reasons_not_to_disclose"]:
        if reason != False:
            world["total"]-=1

    if world["house"]=="Gryffindor":
        world["gryffindor_traits"].append(request.values.get("Gtrait1",False))
        world["gryffindor_traits"].append(request.values.get("Gtrait2", False))
        world["gryffindor_traits"].append(request.values.get("Gtrait3", False))
        world["gryffindor_traits"].append(request.values.get("Gtrait4", False))
        world["gryffindor_traits"].append(request.values.get("Gtrait5", False))
        return render_template("gryffindor_considerations.html", world=world)
    elif world["house"]=="Hufflepuff":
        world["hufflepuff_traits"].append(request.values.get("Htrait1", False))
        world["hufflepuff_traits"].append(request.values.get("Htrait2", False))
        world["hufflepuff_traits"].append(request.values.get("Htrait3", False))
        world["hufflepuff_traits"].append(request.values.get("Htrait4", False))
        world["hufflepuff_traits"].append(request.values.get("Htrait5", False))
        return render_template("hufflepuff_considerations.html", world=world)
    elif world["house"]=="Ravenclaw":
        world["ravenclaw_traits"].append(request.values.get("Rtrait1", False))
        world["ravenclaw_traits"].append(request.values.get("Rtrait2", False))
        world["ravenclaw_traits"].append(request.values.get("Rtrait3", False))
        world["ravenclaw_traits"].append(request.values.get("Rtrait4", False))
        world["ravenclaw_traits"].append(request.values.get("Rtrait5", False))
        return render_template("ravenclaw_considerations.html", world=world)
    elif world["house"]=="Slytherin":
        world["slytherin_traits"].append(request.values.get("Strait1", False))
        world["slytherin_traits"].append(request.values.get("Strait2", False))
        world["slytherin_traits"].append(request.values.get("Strait3", False))
        world["slytherin_traits"].append(request.values.get("Strait4", False))
        world["slytherin_traits"].append(request.values.get("Strait5", False))
        return render_template("slytherin_considerations.html", world=world)




@simple_route('/considerations/results/')
def consideration_results(world:dict, *args): 
    world["considerations_results"]=(request.values.get("disclosing_result"))
    return render_template("considerations_results.html", world=world)