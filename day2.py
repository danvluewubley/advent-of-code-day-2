new_data = []
points = 0
data = open("day2.txt", "r")
data = data.read()

data = data.strip()
data = data.split("\n")

for num in range(0, len(data)):
  new_data.append(data[num].split(' '))

# pt. 1
for i in range(0, len(new_data)):
# wins
  if new_data[i][0] == "A":
    if new_data[i][1] == "Y":
      points = points + 2 + 6
    else:
      pass
  if new_data[i][0] == "B":
    if new_data[i][1] == "Z":
      points = points + 3 + 6
    else:
      pass
  if new_data[i][0] == "C":
    if new_data[i][1] == "X":
      points = points + 1 + 6
    else:
      pass
# draws
  if new_data[i][0] == "A":
    if new_data[i][1] == "X":
      points = points + 1 + 3.
    else:
      pass
  if new_data[i][0] == "B":
    if new_data[i][1] == "Y":
      points = points + 2 + 3
    else:
      pass
  if new_data[i][0] == "C":
    if new_data[i][1] == "Z":
      points = points + 3 + 3
    else:
      pass
# loss
  if new_data[i][0] == "A":
    if new_data[i][1] == "Z":
      points = points + 3
    else:
      pass
  if new_data[i][0] == "B":
    if new_data[i][1] == "X":
      points = points + 1
    else:
      pass
  if new_data[i][0] == "C":
    if new_data[i][1] == "Y":
      points = points + 2
    else:
      pass

print(points)

# pt. 2
points = 0
for i in range(0, len(new_data)):
# if you have to draw
  if new_data[i][1] == "Y":
    if new_data[i][0] == "A":
      points = points + 3 + 1
    if new_data[i][0] == "B":
      points = points + 3 + 2
    if new_data[i][0] == "C":
      points = points + 3 + 3
# if you have to lose
  if new_data[i][1] == "X":
    if new_data[i][0] == "A":
      points = points + 3
    if new_data[i][0] == "B":
      points = points + 1
    if new_data[i][0] == "C":
      points = points + 2
# if you have to win
  if new_data[i][1] == "Z":
    if new_data[i][0] == "A":
      points = points + 6 + 2
    if new_data[i][0] == "B":
      points = points + 6 + 3
    if new_data[i][0] == "C":
      points = points + 6 + 1

print(points)
