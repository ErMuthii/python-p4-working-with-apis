
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://data.cityofchicago.org/resource/ydr8-5enu.json"

    response = requests.get(URL)
    return response.content
  
  def program_school(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
         programs_list.append(program["building_fee_paid"])

    return programs_list

# programs = GetPrograms().get_programs()
# print(programs)
  
programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)