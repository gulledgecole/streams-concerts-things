import functions_framework
from helpers import get_key
from get_concerts import *


@functions_framework.http
def get_concerts(request):
    """Thing to grab concerts from a list of super fun venue ids on a CRON schedule"""
    payload = get_key()
    data, folder_name = bandjame("jambase:6231804", payload)
    print(data)
    print(folder_name)

    return data
