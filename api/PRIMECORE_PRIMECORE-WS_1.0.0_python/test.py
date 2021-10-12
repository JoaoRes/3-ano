from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: default
swagger_client.configuration.access_token = 'VSOuC3OAhd1lruAt7G6cBSwM8zka'
# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.access_point_count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->access_point_count_get: %s\n" % e)
