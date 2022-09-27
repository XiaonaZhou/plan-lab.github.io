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
    
    new_dict['title'] = f'{vals[2]["v"]} ({vals[1]["v"]})' if vals[2] is not None else '-'
    new_dict['h5-index'] = vals[3]['f'] if vals[3] is not None else 'N/A'
    new_dict['core-ranking'] = vals[4]["v"] if vals[4] is not None else '-'
    new_dict['call-for-papers'] = vals[5]["v"] if vals[5] is not None else '-'
    new_dict['abstract-deadline'] = vals[6]['v'] if vals[6] is not None else '-'
    new_dict['submission-deadline'] = vals[7]['v'] if vals[7] is not None else '-'
    new_dict['rebuttal-starts'] = vals[8]['v'] if vals[8] is not None else '-'
    new_dict['notification-date'] = vals[9]['v'] if vals[9] is not None else '-'
    new_dict['conference-date'] = vals[10]['v'] if vals[10] is not None else '-'
    new_dict['conference-location'] = vals[11]['v'] if vals[11] is not None else '-'
    new_dict['tags'] = vals[12]['v'].split(',') if vals[12] is not None else '-'
    new_dict['acceptance-rate-2022'] = vals[13]['v'] if vals[13] is not None else '-'
    new_dict['acceptance-rate-2021'] = vals[14]['v'] if vals[14] is not None else '-'
    new_dict['acceptance-rate-2020'] = vals[15]['v'] if vals[15] is not None else '-'
    new_dict['acceptance-rate-2019'] = vals[16]['v'] if vals[16] is not None else '-'
    
    conf_list.append(new_dict)


    
f = open('./_data/conferences.yaml', 'w')
yaml.dump(conf_list, f)
f.close()