# IBM Action, method=GET, Python 3.9

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    # my IAM_API_KEY
    authenticator = IAMAuthenticator("ng9v3anfOCobH63DPcohiQERqqu4Bdcm-oXVH40ntjU5")
    service = CloudantV1(authenticator=authenticator)
    # my COUCH_URL
    service.set_service_url("https://20c446e9-b7d6-47c4-9aba-260d13815831-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(db='reviews', document=dict["review"]).get_result()
    try:
    # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }
