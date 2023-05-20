from datetime import timedelta
from io import StringIO

from pandas import read_csv


csv_text = """
start_time,end_time,event_name
20230501-1200,20230501-1300,a
20230502-1200,20230502-1400,b
""".strip()


with StringIO(csv_text) as f:
    t = read_csv(f, parse_dates=['start_time', 'end_time'])


print(t)
print()
print(t.dtypes)
print()
print(t['end_time'] - t['start_time'] < timedelta(minutes=90))
