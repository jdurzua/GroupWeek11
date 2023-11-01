def steps(steps):
  average = steps / 7
  if average < 10000:
    print('you did not meet the daily goal')
  elif average == 10000:
    print('you made the goal')
  elif average > 10000:
    print('You exceeded the goal ')