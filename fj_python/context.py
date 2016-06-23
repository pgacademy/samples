
class MyDataFile:
  def __enter__(self):
   // open file
  def __exit__(self, exc_type, exc_value, traceback):
   // close file

file = MyDataFile()
with file:
  file.read()

