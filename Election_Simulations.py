from inspect import EndOfBlock
#generating profiles
def make_IC_profile(num_voters: int, num_alternatives: int):
  alternatives = list(range(num_alternatives))
  profile = []

  for i in range(num_voters):
      random.shuffle(alternatives)
      profile.append(copy.copy(alternatives))

  return profile

#----------------------------Copeland-------------------------------------------

def calculate_Copeland(profile, from_x, to_y):
#LATEST TEST RUN RETURNED ACCURATE RESULTS

  c_from_victories = 0
  c_to_victories = 0
  #Will use these 2 counters to keep track of victories of x vs y

  for i in range(len(profile)):
    x_ballot_pos = -1
    y_ballot_pos = -1 #initializing with value -1

    for j in range(len(profile[i])):
      if (profile[i][j] == from_x):
        x_ballot_pos = j

      if (profile[i][j] == to_y):
        y_ballot_pos = j

    if (x_ballot_pos < y_ballot_pos): c_from_victories += 1 #Less than is the victor in this case
    else: c_to_victories += 1
  
  result = None

  #The logic here is backwards to account for the way counters were summed
  if(c_from_victories > c_to_victories): result = 1
  if(c_from_victories < c_to_victories): result = -1
  if(c_from_victories == c_to_victories): result = 0

  return result

#------------------------------Copeland-----------------------------------------

def Copeland(profile, num_alts):
  #arr_Copeland = [[0]*num_alts] * num_alts  ........ This way references object
# address and causes issues

  arr_Copeland = [[0]*num_alts for i in range(num_alts)]#adjacency matrix I think
#Copeland array generated with 0 in each index

  for i in range(len(arr_Copeland)):
    for j in range(len(arr_Copeland[i])):
      if (i != j):
        arr_Copeland[i][j] = calculate_Copeland(profile, i, j)

  #print(profile)
  #print(arr_Copeland)

  l_copeland_alts = []
  for i in range(len(arr_Copeland)):
    sum_Cope = 0
    for j in range(len(arr_Copeland[i])):
      sum_Cope += arr_Copeland[i][j]

    l_copeland_alts.append(sum_Cope)
#This has summed the rows of the adjency matrix

  #print(l_copeland_alts)

  i_max_C = l_copeland_alts[0]
  i_Copeland_Winner = 0 #If 0 is the winner, this starts at it

  for i in range(len(l_copeland_alts)):
    if(l_copeland_alts[i] > i_max_C):
        i_max_C = l_copeland_alts[i]
        i_Copeland_Winner = i
#Have attained maximum value from the list of copeland values, now check for ties

  tie_checker = 0
  loop_counter = 0
  while(tie_checker < 2 and loop_counter < len(l_copeland_alts)):
    if(i_max_C == l_copeland_alts[loop_counter]):
      tie_checker += 1

    loop_counter += 1
#Have checked for duplicate values for copeland winner

  b_unique_winner = True
  if (tie_checker >= 2):
    b_unique_winner = False

  if (b_unique_winner): return i_Copeland_Winner, True
  else: return i_Copeland_Winner, False #This will signify no unique Condorcet Winner

#--------------------------------Borda------------------------------------------

def calculate_Borda(profile, alternative):
  score = 0

  for i in range(len(profile)):
    for j in range(len(profile[i])): #looking at individual ballot now
      if(profile[i][j] == alternative):
        score += (len(profile[i]) - 1) - j #should sum correct borda values

  return score

#--------------------------------Borda------------------------------------------

def Borda(profile, num_alts):
  l_borda_scores = []

  for i in range(num_alts):
    l_borda_scores.append(calculate_Borda(profile, i))
#Borda scores array has been generated

  #print(l_borda_scores)

  i_max_B = l_borda_scores[0]
  i_Borda_Winner = 0

  for i in range(len(l_borda_scores)):
    if(l_borda_scores[i] > i_max_B):
      i_max_B = l_borda_scores[i]
      i_Borda_Winner = i
#Have attained maximum value from the list of borda values, now check for ties

  tie_checker = 0
  loop_counter = 0
  while(tie_checker < 2 and loop_counter < len(l_borda_scores)):
    if(i_max_B == l_borda_scores[loop_counter]):
      tie_checker += 1

    loop_counter += 1
#Have checked for duplicate values for Borda winner

  b_unique_winner = True
  if (tie_checker >= 2):
    b_unique_winner = False

  if (b_unique_winner): return i_Borda_Winner, True
  else: return i_Borda_Winner, False

#-----------------------------Plurality-----------------------------------------

def calculate_Plurality(profile, alternative):
  score = 0;

  for i in range(len(profile)):
    if(profile[i][0] == alternative): score += 1

  return score

#-----------------------------Plurality-----------------------------------------

def Plurality(profile, num_alts):
  l_plurality_scores = []
  for i in range(num_alts):
    l_plurality_scores.append(calculate_Plurality(profile, i))

  #print(l_plurality_scores)

  i_max_P = l_plurality_scores[0]
  i_Plurality_Winner = 0

  for i in range(len(l_plurality_scores)):
    if(l_plurality_scores[i] > i_max_P):
      i_max_P = l_plurality_scores[i]
      i_Plurality_Winner = i
#Have attained maximum value from the list of borda values, now check for ties

  tie_checker = 0
  loop_counter = 0
  while(tie_checker < 2 and loop_counter < len(l_plurality_scores)):
    if(i_max_P == l_plurality_scores[loop_counter]):
      tie_checker += 1

    loop_counter += 1
#Have checked for duplicate values for Borda winner

  b_unique_winner = True
  if (tie_checker >= 2):
    b_unique_winner = False

  if (b_unique_winner): return i_Plurality_Winner, True
  else: return i_Plurality_Winner, False

#--------------------------Generate Trials--------------------------------------

def generate_Election(num_alts, num_ballots):
  profile = make_IC_profile(num_ballots, num_alts)
#Profile has been generated

#---------------------------Copeland--------------------------------------------

  copeland_winner, condorcet_unique = Copeland(profile, num_alts)
  #if (condorcet_unique): print("Condorcet Winner: " + str(copeland_winner))
  #else: print("No unique Condorcet Winner, Copeland Winner: " + str(copeland_winner))

#-------------------------------Borda-------------------------------------------

  borda_winner, borda_unique = Borda(profile, num_alts)
  #if (borda_unique): print("Borda Winner: " + str(borda_winner))
  #else: print("Non-unique Borda Winner: " + str(borda_winner))

#-------------------------------Plurality---------------------------------------

  plurality_winner, plurality_unique = Plurality(profile, num_alts)
  #if (plurality_unique): print("Plurality Winner: " + str(plurality_winner))
  #else: print("Non-unique Plurality Winner: " + str(plurality_winner))

#------------------------------Comparisons--------------------------------------

  #NEED TO IMPLEMENT A FAILSAFE FOR WHEN THE TESTS RETURN NON-UNIQUE WINNERS,
  #E.G. NEED TO KNOW WHEN IT IS A TIED VALUE, BUT STILL WANT TO RETURN THE WINNER(S)
  #INSTEAD OF JUST RETURNING AN ARBITRARY -1

  #Going to return 3 values for a graph
  c_unique_condorcet = 0
  copeland_borda_comparison = 0
  copeland_plurality_comparison = 0
  borda_plurality_copeland_agreement = 0

  if(condorcet_unique):
    c_unique_condorcet = 1
    if(copeland_winner == borda_winner): copeland_borda_comparison = 1
    else: copeland_borda_comparison = 0

    if(copeland_winner == plurality_winner): copeland_plurality_comparison = 1
    else: copeland_plurality_comparison = 0

  else:
    if(copeland_winner == borda_winner == plurality_winner): 
      borda_plurality_copeland_agreement = 1
    else: borda_plurality_copeland_agreement = 0

  return c_unique_condorcet, copeland_borda_comparison, copeland_plurality_comparison, borda_plurality_copeland_agreement
  
#--------------------------------Graph Generate Points--------------------------

def calculate_Frequencies(num_alts, num_ballots, num_profiles):

  condorcet_counter = 0
  no_condorcet_counter = 0
  condorcet_equal_borda_counter = 0
  condorcet_equal_plurality_counter = 0
  cope_borda_plurality_agreement_counter = 0

  for i in range(num_profiles):
    unique_condorcet, borda_agreement, plurality_agreement, b_coincide = generate_Election(num_alts, num_ballots)
    condorcet_counter += unique_condorcet
    if(unique_condorcet == 0):
      cope_borda_plurality_agreement_counter += b_coincide
      no_condorcet_counter += 1
    else:
      condorcet_equal_borda_counter += borda_agreement
      condorcet_equal_plurality_counter += plurality_agreement


  #print(condorcet_counter)

  array_points_frequency = []
  array_points_frequency.append(condorcet_counter / num_profiles)
  array_points_frequency.append(condorcet_equal_borda_counter / num_profiles)
  array_points_frequency.append(condorcet_equal_plurality_counter / num_profiles)
  array_points_frequency.append(cope_borda_plurality_agreement_counter / no_condorcet_counter)

  return array_points_frequency



def main():
  import matplotlib.pyplot as plt
  import random
  import copy
  import numpy as np

  num_alts = [10, 12, 15]
  num_ballots = [10, 20, 30, 40, 50]
  num_profiles = 10000

  x_plot_num_voters = []
  y_frequencies = []
  y_condorcet = [[0]*len(num_alts) for i in range(len(num_ballots))]
  y_borda = [[0]*len(num_alts) for i in range(len(num_ballots))]
  y_plurality = [[0]*len(num_alts) for i in range(len(num_ballots))]
  y_coincide = [[0]*len(num_alts) for i in range(len(num_ballots))]

  for i in range(len(num_ballots)):
    x_plot_num_voters.append(num_ballots[i])
    for j in range(len(num_alts)):
      y_frequencies = calculate_Frequencies(num_alts[j], num_ballots[i], num_profiles);
      y_condorcet[i][j] = y_frequencies[0]
      y_borda[i][j] = y_frequencies[1]
      y_plurality[i][j] = y_frequencies[2]
      y_coincide[i][j] = y_frequencies[3]

  labels = ["m = 10", "m = 12", "m = 15"]
  #labels are for the graph legend

  plt.plot(x_plot_num_voters, y_condorcet)
  plt.xlabel("Number of Ballots per Profile")
  plt.ylabel("Frequency of Occurence (per " + str(num_profiles) + " profiles)")
  plt.title("Existence of a Condorcet Winner")
  plt.legend(labels)
  plt.show()
  plt.savefig("Cond")
#fig = plt.gcf();
#fig.savefig("Condorcet_Winner.png")

  plt.plot(x_plot_num_voters, y_borda)
  plt.xlabel("Number of Ballots per Profile")
  plt.ylabel("Frequency of Occurence (per " + str(num_profiles) + " profiles)")
  plt.title("Borda Selecting the Condorcet Winner")
  plt.legend(labels)
  plt.show()

  plt.plot(x_plot_num_voters, y_plurality)
  plt.xlabel("Number of Ballots per Profile")
  plt.ylabel("Frequency of Occurence (per " + str(num_profiles) + " profiles)")
  plt.title("Plurality Selecting the Condorcet Winner")
  plt.legend(labels)
  plt.show()

  plt.plot(x_plot_num_voters, y_coincide)
  plt.xlabel("Number of Ballots per Profile")
  plt.ylabel("Frequency of Occurence (per " + str(num_profiles) + " profiles)")
  plt.title("In the Absence of a Condorcet Winner, CO, B, P Coincide")
  plt.legend(labels)
  plt.show()
