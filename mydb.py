from country import Country
from user import User
from job import Job
class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.User=User()
    self.Job=Job()
