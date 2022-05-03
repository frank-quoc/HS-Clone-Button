import re

from dateutil.relativedelta import relativedelta
from datetime import datetime
from calendar import timegm

def make_payload(json_data):
    new_timestamp = add_1_year(json_data["properties"].get("closedate", {}).get("value", ""))

    return {"properties": {
                "closedate": new_timestamp,
                "dealname": f'{remove_date_in_name(json_data["properties"].get("dealname", {}).get("value", ""))}: {datetime.utcfromtimestamp(new_timestamp//1000).strftime("%b %d, %Y")}',
                "amount": json_data["properties"].get("amount", {}).get("value", ""),
                "dealstage": json_data["properties"].get("dealstage", {}).get("value", ""),
                "hubspot_owner_id": json_data["properties"].get("hubspot_owner_id", {}).get("value", ""),
                "pipeline": json_data["properties"].get("pipeline", {}).get("value", ""),
                }
            }

def add_1_year(timestamp):
    if timestamp == "":
        timestamp = return_unix_time(datetime.now())
    close_date = datetime.utcfromtimestamp(int(timestamp)//1000).replace(microsecond=int(timestamp)%1000*1000)
    new_date = close_date + relativedelta(years=1)
    return return_unix_time(new_date) 

def return_unix_time(date_time):
    return timegm(date_time.timetuple()) * 1000

def remove_date_in_name(deal_name):
    return re.sub("([:]\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4})$", "", deal_name).strip()
