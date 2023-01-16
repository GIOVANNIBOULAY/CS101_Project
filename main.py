from algorithms import *
from datetime import datetime

def welcome():
    print(
        """
    THE DOJO CLUB® ALGORITHMS
    welcome, agent.
    """)

def path():
    agent_input = ""
    while agent_input == "":
        agent_input = input("ENTER CODE \n > ")
    return agent_input.upper().strip()

def check_path(path):
    if path.upper().strip() == 'STRUCTURE':
        structure_algo()
    elif path.upper().strip() == 'DOCUMENTATION':
        documentation_algo()
    elif path.upper().strip() == 'MEETINGS':
        meetings_algo()
    elif path.upper().strip() == 'INSTACART':
        instacart_algo()
    elif path.upper().strip() == 'MISSION':
        mission_algo()
    elif path.upper().strip() == 'SAMU':
        samu_algo()
    elif path.upper().strip() == 'WAKE':
        wake_algo()
    elif path.upper().strip() == 'EXERCISE':
        exercise_algo()

def structure_algo():
    print(structure_menu)
    agent_input = input("STRUCTURE > ")
    if agent_input.upper().strip() == "EXORDIUM":
        print(exordium)
    elif agent_input.upper().strip() == "DIRECTION":
        print(direction)
    elif agent_input.upper().strip() == "EXECUTION":
        print(execution)
    elif agent_input.upper().strip() == "TECHNIQUE":
        print(technique)
    elif agent_input.upper().strip() == "BOTTOM-UP":
        print(bottom_up)

def documentation_algo():
    print(documentation_menu)
    agent_input = input("DOCUMENTATION > ")
    if agent_input.upper().strip() == "UNDERSTANDING":
        print(understanding_the_numbers)
    elif agent_input.upper().strip() == "WHEN":
        print(when_to_document)
    elif agent_input.upper().strip() == "WHERE":
        print(where_to_document)

def meetings_algo():
    print(documentation_menu)
    agent_input = input("DOCUMENTATION > ")
    if agent_input.upper().strip() == "FINANCE":
        print(daily_finance)

def instacart_algo():
    print(instacart_menu)
    agent_input = input("INSTACART > ")
    if agent_input.upper().strip() == "HOURS":
        print(instacart_hours)
    elif agent_input.upper().strip() == "RESTRICTIONS":
        print(instacart_restrictions)
    elif agent_input.upper().strip() == "CRITERIA":
        print(instacart_criteria)
    elif agent_input.upper().strip() == "ACCEPTED":
        accepted_input = input("IS IT THE FIRST BATCH OF THE DAY? (y/n) > ")
        if accepted_input.upper().strip() == "Y" or accepted_input.upper().strip() == "YES":
            print(instacart_first_accepted)
        elif accepted_input.upper().strip() == "N" or accepted_input.upper().strip() == "NO":
            print(instacart_accepted)
    elif agent_input.upper().strip() == "END OF SHIFT":
        print("send thanks for tips for all batches")

def mission_algo():
    print(current_mission)
    agent_input = input("MISSION > ")
    if agent_input.upper().strip() == "WHAT TO LEARN":
        print(what_to_learn)
    elif agent_input.upper().strip() == "UNDERSTANDING":
        print(maximizing_understanding)
    elif agent_input.upper().strip() == "PORTFOLIO":
        print(portfolio_projects)
    elif agent_input.upper().strip() == "JOBS":
        print(applying_for_jobs)

def wake_algo():
    print(wake_menu)

def samu_algo():
    print(samu_menu)
    agent_input = input("SAMU > ")
    if agent_input.upper().strip() == "KITCHEN":
        print(kitchen_samu)
    elif agent_input.upper().strip() == "BEDROOM":
        print(bedroom_samu)
    elif agent_input.upper().strip() == "BATHROOM":
        print(bathroom_samu)

def exercise_algo():
    today = datetime.now()
    day_of_week = today.strftime('%A')
    if day_of_week == "Monday":
        print(day_of_week.upper() + ": UPPER BODY WORKOUT")
    elif day_of_week == "Tuesday":
        print(day_of_week.upper() + ": UPPER BODY YOGA")
    elif day_of_week == "Wednesday":
        print(day_of_week.upper() + ": LOWER BODY WORKOUT")
    elif day_of_week == "Tuesday":
        print(day_of_week.upper() + ": LOWER BODY YOGA")
    elif day_of_week == "Friday":
        print(day_of_week.upper() + ": CORE WORKOUT")
    elif day_of_week == "SATURDAY":
        print(day_of_week.upper() + ": FULL BODY YOGA")
    elif day_of_week == "SUNDAY":
        print(day_of_week.upper() + ": REST")

main_menu = 1
while main_menu != 0:
    welcome()
    path_taken = path()
    check_path(path_taken)
    main_menu = int(input("""
'0' end
'1' main menu
> """))

print("godspeed.")