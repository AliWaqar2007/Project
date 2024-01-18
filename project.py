t_overs = int(input("Enter the total overs bowled: "))
no_of_batsmen = int(input("Enter the number of batsmen who batted: "))
if no_of_batsmen>11:
    print("Batsmen cannot be more than 11")
else:    
    no_of_bowlers = int(input("Enter the number of bowlers: "))

total_score = 0
total_wickets = 0
total_overs = 0
t_bowls = 0
batsmen_data = []
bowlers_data = []

for i in range(no_of_bowlers):
    if no_of_bowlers>10:
        print("Sorry! Bowlers cannot be more than 10")
    else:
        bowler_name = input("Enter the name of the bowler: ")
        overs_bowled = int(input("Enter the number of overs bowled by him: "))
        runs_conceded = int(input("Enter the amount of runs he conceded: "))
        wickets_taken = int(input("Enter the number of wickets taken by him: "))
        extras = int(input("Enter the total number of wide balls and no balls altogether: "))

    bowler_data = [bowler_name, overs_bowled, runs_conceded, wickets_taken, extras]
    bowlers_data.append(bowler_data)
    total_score += extras
    total_wickets += wickets_taken

for i in range(no_of_batsmen):
    batsman_name = input("Enter the name of the batsman: ")
    batsman_score = int(input("Enter the amount of runs he scored: "))
    bowls_played = int(input("Enter the number of balls he played: "))
    t_bowls +=bowls_played
    
    if bowls_played>(t_overs*6):
        print("Sorry! Batsman cannot play balls more than",(t_overs*6))
    else:    
        six = int(input("Enter the number of sixes he hit: "))
        four = int(input("Enter the number of fours he hit: "))

    strike_rate = round((batsman_score/bowls_played)*100)
    batsman_data = [batsman_name, batsman_score, bowls_played, six, four, strike_rate]
    batsmen_data.append(batsman_data)
    total_score += batsman_score

run_rate = total_score/t_overs

if t_bowls!=(t_overs*6):
    print("Bowls played by all batters should sum up to",(t_overs*6))
else:
    print("\n\nTotal score and wickets in",t_overs,": ",total_score,"/",total_wickets,"\n\n")
    print("\n\nRun Rate:", run_rate)
    print("Batting side performance:\n")
    for batsman_data in batsmen_data:
        print("\nBatsman name:", batsman_data[0])
        print("Batsman score:", batsman_data[1])
        print("Bowls Played:", batsman_data[2])
        print("Six:", batsman_data[3])
        print("Four:", batsman_data[4])
        print("Strike Rate:", batsman_data[5])

    print("\nBowling side performance:\n")
    for bowler_data in bowlers_data:
        print("\nBowler name:", bowler_data[0])
        print("Overs bowled:", bowler_data[1])
        print("Runs conceded:", bowler_data[2])
        print("Wickets taken:", bowler_data[3])
        print("Extras:", bowler_data[4])
