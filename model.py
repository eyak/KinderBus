from pyairtable.orm import Model, fields as F
from settings import *

class Registration(Model):
    name = F.LinkField("Name", "Kid")
    date  = F.DateField("Date")
    action = F.SelectField("Action")
    direction = F.SelectField("Direction")
    created = F.CreatedTimeField("Created")

    class Meta:
        table_name = "הסעות"
        api_key = AIRTABLE_API_KEY
        base_id = AIRTABLE_BUS_BASE_ID

class Kid(Model):
    name = F.TextField("Name")

    class Meta:
        table_name = "Kids"
        api_key = AIRTABLE_API_KEY
        base_id = AIRTABLE_BUS_BASE_ID