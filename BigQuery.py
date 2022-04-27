from google.cloud import bigquery
import os 

credentials_path = 'location/filename.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'project.dataset.table_name'

rows_to_insert = [
    {u'sensorName':'garden-001', u'tenperature':88.0, u'humidity':32.1},
    {u'sensorName':'garden-002', u'tenperature':90.2, u'humidity':34.0},
]

errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print('New rows have been added.')
else:
    print('Encountered errors while inserting rows: {errors}')

