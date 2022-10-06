from dataclasses import dataclass, field
from typing import List
from pprint import pprint as pp

schedule_file = "Выборг.SCH"

stations = {}

@dataclass
class Stop:
    name: str
    arrive: str
    depart: str


@dataclass
class Train:
    name: str = None
    rank: str = None
    enter: str = None
    stops: List[Stop] = field(default_factory=list)


def parse_train_details(file, line:str):
    name = extract_name(sch_line)

    ##while len (sch_line := file.readline() )  < 5:

    if name in trains:
        name = name + 'Δ'
    
    trains[name] = '+'
    print('\n', name)

    #Sub loop to get Train property
    ##sch_line = sch.readline()
    ##if not sch_line: break
    '''
    while sch_line := sch.readline():
        sch_line = sch_line.strip()
        if sch_line.startswith("Train:"):

    '''


with open(schedule_file, encoding='1251') as sch:
    trains = []
    status = 0  #outside Train
    t = Train()

    while sch_line := sch.readline():
        sch_line = sch_line.strip()
        if not sch_line or len(sch_line) < 6 or sch_line.startswith('#'):
            continue

        pair = sch_line.split(":", 1)
        match pair:
            case 'Train', name:
                if status:
                    #End old Train
                    trains.append(t)
                    t = Train()
                status = 1  #inside Train           
                t.name = name
                continue
            case 'Type', rank:
                t.rank = rank
                continue
            case 'Enter', enter_str:
                t.enter = enter_str
                continue

        print(sch_line)
        

pp(trains[-10:-2])
