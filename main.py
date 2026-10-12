import project_2

while True:
    
    print("+"*60)
    print("          Football analyzer: ")
    print("+"*60)
    
    #menu
    
    print("1. Reading CSV file")
    print("2. Data Cleaning")
    print("3. Home goals vs Away goals")
    print("4. Do you want top 5 home/away ground and bottom 5 home/away ground goals")
    print("5. Minimum goals and Maximum goals")
    print("6. Team details")
    print("7. Pivot table")
    print("8. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        project_2.reading_csv()
        
    elif choice == 2:
        project_2.Data_Cleaning()
        
    elif choice == 3:
        goals = int(input("Enter the number of goals: "))
        teams = input("Enter the team name: ").split(",")
        teams = [team.strip() for team in teams]
        project_2.home_away_goals(goals,teams)
        
    elif choice == 4:
        project_2.top_bottom_5()
        
    elif choice == 5:
        mini_goals = int(input("Enter minimum number of goals: "))
        maxi_goals = int(input("Enter maximum number of goals: "))
        
        project_2.goals(mini_goals,maxi_goals)
        
    elif choice ==6:
        team = input("Enter team name: ").lower()
        
        project_2.team_name(team)
        
    elif choice == 7:
        
        project_2.pivot_table()
        
    elif choice == 8:
        break
        
        
        
        