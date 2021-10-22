#! /usr/bin/env python3

import os
import requests

feedback = '/data/feedback'
url = 'http://35.223.89.129/feedback/' 

files = os.listdir(feedback)

for file in files:
  file_obj = open(os.path.join(feedback, file), 'r')

  lines = [ line.replace('\n', '') for line in file_obj ]

  feedback_dict = { "title": lines[0], "name": lines[1], "date": lines[2], "feedback": lines[3] }

  res = requests.post(url, data=feedback_dict)

  if not res.status_code == 201:
    print('Something went wrong')

  file_obj.close()
