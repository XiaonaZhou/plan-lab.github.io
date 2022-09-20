import json
import requests
import yaml
from urllib.parse import quote

# sheet_id = '1dzx8QSiBQFcUOQTPa_uI64OCGQqESWtrq6EwqOVngZw'
sheet_id = '1z49Gu0j6Lc6AcZjyjDR6BGUgcjEuTqcO5Vxp8ZCAZxM'
base = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?'
# https://docs.google.com/spreadsheets/d/1dzx8QSiBQFcUOQTPa_uI64OCGQqESWtrq6EwqOVngZw/gviz/tq?

sheet_name = 'user-data'
query = quote('Select *')
url = f'{base}&sheet=${sheet_name}&tq={query}'

print(url)

x = requests.get(url)
sheets_data = json.loads('('.join(x.text.split('\n')[1].split('(')[1:])[:-2])

conf_list = []

for idx, row in enumerate(sheets_data['table']['rows']):
    vals = row['c']
    new_dict = {}
    if idx == 0:
        continue
    
    new_dict['title'] = f'{vals[2]["v"]} ({vals[1]["v"]})'
    new_dict['h5-index'] = vals[3]['f'] if vals[3] is not None else 'N/A'
    new_dict['core-ranking'] = vals[4]["v"]
    new_dict['call-for-papers'] = vals[5]["v"]
    new_dict['abstract-deadline'] = vals[6]['v']
    new_dict['submission-deadline'] = vals[7]['v']
    new_dict['rebuttal-starts'] = vals[8]['v']
    new_dict['notification-date'] = vals[9]['v']
    new_dict['conference-date'] = vals[10]['v']
    new_dict['conference-location'] = vals[11]['v']
    new_dict['tags'] = vals[12]['v'].split(',')
    new_dict['acceptance-rate-2022'] = vals[13]['v']
    new_dict['acceptance-rate-2021'] = vals[14]['v']
    new_dict['acceptance-rate-2020'] = vals[15]['v']
    new_dict['acceptance-rate-2019'] = vals[16]['v']
    
    conf_list.append(new_dict)


    
f = open('./_data/conferences.yaml', 'w')
yaml.dump(conf_list, f)
f.close()