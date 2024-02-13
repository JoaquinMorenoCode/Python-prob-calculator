import copy
import random

# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs) -> None:
    self.contents = []
    self.drawObjetcs = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, n):

    if (n > len(self.contents)):
      return self.contents
    for i in range(n):
      # print(i)
      getRamdomIndex = random.randint(0, len(self.contents) - 1)
      # print("lenContents: {}".format(len(self.contents)-1))

      # print("randomN: {}".format(getRamdomIndex))

      self.drawObjetcs.append(self.contents.pop(getRamdomIndex))

      # print("draw balls: {}".format(self.drawObjetcs))
    return self.drawObjetcs

  def __str__(self) -> str:
    return "".join(str(self.contents))


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn,
               num_experiments):
  matches = 0
  i = 0
  if (num_balls_drawn > len(hat.contents)):
    return 1.0

  while i < num_experiments:
    count = 0
    copyHat = copy.deepcopy(hat)
    currentDraw = copyHat.draw(num_balls_drawn)
    # print("currentDraw {}".format(currentDraw))
    test = {}
    for ball in currentDraw:
      # print("currentBall {}".format(ball))
      if (ball in test):
        test[ball] += 1
      else:
        test[ball] = test.get(ball, 1)

    # print("test: {}".format(test))
    for key, value in expected_balls.items():
      # print("currentKey {}".format(key))
      if test.get(key, 0) >= value:
        count += 1

    if (count == len(expected_balls)):
      # print("MATCH?: {}".format(test))
      matches += 1

    i += 1
  probability = matches / num_experiments
  return (probability)
