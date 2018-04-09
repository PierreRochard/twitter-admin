import json
import os
from collections import defaultdict

path = 'followers'
followers = []
for doc in os.listdir(path):
    with open(os.path.join(path, doc), 'r') as fp:
        follower = json.load(fp)
        followers.append(follower)

columns = defaultdict(dict)
for follower in followers:
    for key, value in follower.items():
        value_type = str(type(value).__name__)
        if value is not None and columns[key].get('value_type', None) and columns[key]['value_type'] != value_type:
            raise Exception(f'inconsistent type for {key}')
        if value is not None:
            columns[key]['value_type'] = value_type
        if value is None:
            columns[key]['nullable'] = True
        else:
            columns[key]['sample'] = value

type_map = {
    'int': 'BIGINT',
    'dict': 'JSONB',
    'str': 'String',
    'bool': 'Boolean'
}

type_overrides = {
    'created_at': 'DateTime'
}


for column in columns:
    column_type = type_overrides.get(column, type_map[columns[column]["value_type"]])
    nullable = columns[column].get('nullable', False)
    print(f'{column} = Column({column_type}, nullable={nullable})')

print(doc)
