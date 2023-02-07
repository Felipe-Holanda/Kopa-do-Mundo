from datetime import datetime


class NegativeTitlesError(Exception):
    ...

class InvalidYearCupError(Exception):
    ...

class ImpossibleTitlesError(Exception):
    ...

first_cup = datetime(1930, 7, 13)

def data_processing(data):
    
    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative");

    first_cup_team = datetime.strptime(data["first_cup"], "%Y-%m-%d")

    if first_cup_team < first_cup or (first_cup_team.year - first_cup.year) % 4 != 0 :
        raise InvalidYearCupError("there was no world cup this year");

    amout_possible_titles = (datetime.now().year - first_cup_team.year) / 4;

    if data["titles"] > amout_possible_titles:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups");

    return data;


