class EggApplication(Exception):
  """hoge"""

class TooBakedEggError(EggApplication):
  """hoge"""


try:
  raise TooBakedEggError("1 hour")
except EggApplication as e:
  print(e)


print("end")


class Pan:

  def bake(egg, time):
    raise TooBakedEggError()


class Chef:

  def cook(foods):

    pan = Pan();
    try:
      pan.bake(egg, 300)
    except EggApplication as e
      gomibako.put(egg)
      raise e

    # ...



chef = Chef()

try:
  chef.cook()
except EggApplication as e
  print("調理失敗しました")





