import random

# Real ICC squads (sample players, can be expanded)
ICC_TEAMS = {
    "India": {
        "batsmen": ["Rohit Sharma", "Virat Kohli", "Shubman Gill", "Suryakumar Yadav"],
        "allrounders": ["Hardik Pandya", "Ravindra Jadeja", "Axar Patel"],
        "fast_bowlers": ["Jasprit Bumrah", "Mohammed Shami", "Mohammed Siraj"],
        "spinners": ["Kuldeep Yadav", "Ravi Bishnoi"]
    },
    "Australia": {
        "batsmen": ["David Warner", "Steve Smith", "Marnus Labuschagne", "Travis Head"],
        "allrounders": ["Glenn Maxwell", "Mitchell Marsh", "Marcus Stoinis"],
        "fast_bowlers": ["Pat Cummins", "Josh Hazlewood", "Mitchell Starc"],
        "spinners": ["Adam Zampa", "Nathan Lyon"]
    },
}

MATCH_FORMATS = {"T10": 10, "T20": 20, "ODI": 50, "Hundred": 100}
SPIN_FRIENDLY_PITCHES = ["spin"]
STADIUMS = {"India": "Wankhede Stadium", "Australia": "Melbourne Cricket Ground"}

def select_playing_xi(team_name, pitch_type):
    team = ICC_TEAMS.get(team_name)
    if not team:
        print(f"Team {team_name} not found!")
        return None
    
    batsmen = team["batsmen"]
    allrounders = team["allrounders"]
    fast_bowlers = team["fast_bowlers"]
    spinners = team["spinners"]
    
    if pitch_type in SPIN_FRIENDLY_PITCHES:
        return batsmen[:4] + allrounders[:3] + fast_bowlers[:2] + spinners[:3]
    else:
        return batsmen[:4] + allrounders[:3] + fast_bowlers[:3] + spinners[:2]

def toss():
    return random.choice(["bat", "bowl"])

def simulate_innings(max_overs, target=None):
    total_runs, wickets, balls = 0, 0, 0
    for over in range(max_overs):
        if wickets >= 10:
            break
        for ball in range(6):
            if wickets >= 10:
                break
            outcome = random.choice([0, 1, 2, 3, 4, 6, "W"])
            balls += 1
            if outcome == "W":
                wickets += 1
            else:
                total_runs += outcome
            print(f"Over {over + 1}.{ball + 1}: {outcome} runs")
            
            if target and total_runs > target:
                print(f"Target reached in {balls // 6}.{balls % 6} overs!")
                return total_runs, wickets, balls
        
        overs_completed = balls // 6
        remaining_balls = balls % 6
        print(f"End of Over {overs_completed}.{remaining_balls}: {total_runs}/{wickets}\n")
    
    return total_runs, wickets, balls

def simulate_match(fav_team, opp_team, format_type, pitch_type, venue):
    print(f"\nMatch Format: {format_type} | Pitch: {pitch_type} | Venue: {venue}\n")
    
    fav_team_xi = select_playing_xi(fav_team, pitch_type)
    opp_team_xi = select_playing_xi(opp_team, pitch_type)
    if not fav_team_xi or not opp_team_xi:
        print("Error selecting playing XIs.")
        return
    
    print(f"\n{fav_team} Playing XI: {fav_team_xi}")
    print(f"{opp_team} Playing XI: {opp_team_xi}")
    
    toss_winner = random.choice([fav_team, opp_team])
    toss_decision = toss()
    print(f"\n{toss_winner} won the toss and chose to {toss_decision} first!")
    
    first_batting, first_bowling = (toss_winner, opp_team) if toss_decision == "bat" else (opp_team, toss_winner)
    
    print(f"\n{first_batting} is batting first!")
    first_innings_score, first_wickets, first_balls = simulate_innings(MATCH_FORMATS[format_type])
    first_overs_completed = first_balls // 6
    first_remaining_balls = first_balls % 6
    print(f"{first_batting} scored {first_innings_score}/{first_wickets} in {first_overs_completed}.{first_remaining_balls} overs\n")
    
    print(f"{first_bowling} now needs {first_innings_score + 1} runs to win!\n")
    second_innings_score, second_wickets, second_balls = simulate_innings(MATCH_FORMATS[format_type], target=first_innings_score)
    second_overs_completed = second_balls // 6
    second_remaining_balls = second_balls % 6
    print(f"{first_bowling} scored {second_innings_score}/{second_wickets} in {second_overs_completed}.{second_remaining_balls} overs\n")
    
    if second_innings_score > first_innings_score:
        print(f"{first_bowling} wins by {10 - second_wickets} wickets!")
    elif second_innings_score < first_innings_score:
        print(f"{first_batting} wins by {first_innings_score - second_innings_score} runs!")
    else:
        print("It's a tie!")

def main():
    fav_team = "India"
    opp_team = "Australia"
    format_type = "T20"
    pitch_type = "flat"
    home_or_away = "home"
    venue = STADIUMS.get(fav_team) if home_or_away == "home" else STADIUMS.get(opp_team, "Neutral Venue")
    simulate_match(fav_team, opp_team, format_type, pitch_type, venue)

if __name__ == "__main__":
    main()