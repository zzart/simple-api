""" Helper functions for dealing with JSON and time conversions """

import datetime
import decimal
import uuid
import json
from typing import Any


def json_handler(obj: Any)-> str:
    """
    Json Handler for formatting different python types into json
    :param obj: object of any type which needs to be serialized to json
    :return: json serializable type
    """
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    if isinstance(obj, (decimal.Decimal, uuid.UUID)):
        return "{}".format(obj)
    if isinstance(obj, set):
        return ", ".join(obj)
    return json.JSONEncoder().default(obj)


