letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# 1 Combining 2 lists with a list comprehension 

#new dict
letter_to_points = {key: value for key,value in zip(letters,points)}

#adding blank tiles in the game 
letter_to_points[" "] = 0

#Writing a func to take a word and returns how many points we get per word.

def score_word(word):
  point_total = 0
  for i in word:
    point_total += letter_to_points.get(i,0)
    return point_total

brownie_points = score_word("BROWNIE")

print(brownie_points)

#another dict.:MAPS players to a list of the words they have played

player_to_words = {
  "player1":["BLUE","TENNIS","EXIT"],
  "wordNerd":["EARTH","EYES","MACHINE"],
  "Lexi Con":["ERASER","BELLY","HUSKY"],
  "rof Reader":["ZAP","COMA","PERIOD"]
}

#An empty dict.

player_to_points = {}

#iterating through player_to_word
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)
