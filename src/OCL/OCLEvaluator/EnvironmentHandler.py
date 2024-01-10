from OCL.utils.utils import *
from OCL.Environment.Environment import *
class EnvironmentHandler:
    env = Environment()
    def populateEnvironment(self, OD_path):
      populateOD(self.env,OD_path)

    def print(self):
        self.env.print()
    def getAllInstances(self,className):
        return self.env.getallInstance(className)