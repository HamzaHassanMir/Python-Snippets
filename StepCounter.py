print("STEP COUNTER")

daily_goal = int(input("Enter your daily step goal: "))
current_steps = int(input("Enter the number of steps you have taken today: "))
remaining_steps = daily_goal - current_steps

if remaining_steps > 0:
  print(f"You have {remaining_steps} steps remaining today.")
else:
  print("You have met your daily step goal.")