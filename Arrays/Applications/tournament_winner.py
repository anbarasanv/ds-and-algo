""" 
  ┌────────────────────────────────────────────────────────────────────────────┐
  │ There's an algorithms tournament taking place in which teams of            │
  │ programmers                                                                │
  │ compete against each other to solve algorithmic problems as fast as        │
  │ possible.                                                                  │
  │ Teams compete in a round robin, where each team faces off against all      │
  │ other teams.                                                               │
  │ Only two teams compete against each other at a time, and for each          │
  │ competition,                                                               │
  │ one team is designated the home team, while the other team is the away     │
  │ team.                                                                      │
  │ In each competition there's always one winner and one loser; there are no  │
  │ ties.                                                                      │
  │ A team receives 3 points if it wins and 0 points if it loses.              │
  │ The winner of the tournament is the team that receives the most amount of  │
  │ points.                                                                    │
  │                                                                            │
  │ Given an array of pairs representing the teams that have competed against  │
  │ each other                                                                 │
  │ and an array containing the results of each competition, write a function  │
  │ that returns                                                               │
  │ the winner of the tournament. The input arrays are named competitions and  │
  │ results, respectively.                                                     │
  │ The competitions array has elements in the form of [homeTeam, awayTeam],   │
  │ where each team is a string of at most 30 characters representing the      │
  │ name of the team.                                                          │
  │ The results array contains information about the winner of each            │
  │ corresponding                                                              │
  │ competition in the competitions array. Specifically,                       │
  │ results[i] denotes the winner of competitions[i],                          │
  │ where a 1 in the results array means that the home team in                 │
  │ the corresponding competition won and a 0 means that the away team won.    │
  │ It's guaranteed that exactly one team will win the tournament and that     │
  │ each team will compete                                                     │
  │ against all other teams exactly once.                                      │
  │ It's also guaranteed that the tournament will always have at least two     │
  │ teams.                                                                     │
  ├────────────────────────────────────────────────────────────────────────────┤
  │ competitions = [                                                           │
  │   ["HTML", "C#"],                                                          │
  │   ["C#", "Python"],                                                        │
  │   ["Python", "HTML"],                                                      │
  │ ]                                                                          │
  │ results = [0, 0, 1]                                                        │
  ├────────────────────────────────────────────────────────────────────────────┤
  │ "Python"                                                                   │
  │ // C# beats HTML, Python Beats C#, and Python Beats HTML.                  │
  │ // HTML - 0 points                                                         │
  │ // C# -  3 points                                                          │
  │ // Python -  6 points                                                      │
  │                                                                            │
  └────────────────────────────────────────────────────────────────────────────┘
"""


def tournament_winner(competitions, results):
    """
    >>> tournament_winner([["HTML", "C#"],["C#", "Python"],
    ... ["Python", "HTML"]],[0, 0, 1])
    'Python'
    """
    teams = {}
    winning_team_val = 0
    winning_team_name = ""

    for team, result in zip(competitions, results):
        if result == 1:
            if team[0] not in teams:
                teams[team[0]] = 0
            teams[team[0]] += 3
            temp_team_name = team[0]
            temp_team_val = teams[team[0]]
        else:
            if team[1] not in teams:
                teams[team[1]] = 0
            teams[team[1]] += 3
            temp_team_name = team[1]
            temp_team_val = teams[team[1]]

        # Set the winning team val to the current value.
        if temp_team_val > winning_team_val:
            winning_team_val = temp_team_val
            winning_team_name = temp_team_name

    return winning_team_name
