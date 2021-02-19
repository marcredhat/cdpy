from cdpy.cdpy import Cdpy
import ipdb
from cdpy.environments import CdpyEnvironments
from cdpy.dw import CdpyDw
from cdpy.common import CdpSdkBase, Squelch, CdpError
sdk = CdpyEnvironments()
#ipdb.set_trace()
print(sdk.describe_all_environments())
print(sdk.summarize_environment("marccdp"))
#RESULT:
#[{'environmentName': 'marccdp', 'crn': 'crn:altus:environments:us-west-1:27c485f2-d664-4a62-911c-8454d5ea311a:environment:marccdp/5b56f5d8-6089-43f6-96bb-fa67e9d3ba44', 'status': 'AVAILABLE', 'cloudPlatform': 'OPENSHIFT'}]
#{'environmentName': 'marccdp', 'crn': 'crn:altus:environments:us-west-1:27c485f2-d664-4a62-911c-8454d5ea311a:environment:marccdp/5b56f5d8-6089-43f6-96bb-fa67e9d3ba44', 'status': 'AVAILABLE', 'cloudPlatform': 'OPENSHIFT'}

cdpy.common.CdpError: CdpError('Supplied env_crn crn:altus:environments:us-west-1:27c485f2-d664-4a62-911c-8454d5ea311a:environment:marccdp/5b56f5d8-6089-43f6-96bb-fa67e9d3ba44 is not a valid CDP Environment crn',)

sdk = CdpyDw()
print(sdk.gather_clusters("crn:altus:environments:us-west-1:27c485f2-d664-4a62-911c-8454d5ea311a:environment:marccdp/5b56f5d8-6089-43f6-96bb-fa67e9d3ba44"))
#RESULT (NOK)
#cdpy.common.CdpError: CdpError('Supplied env_crn crn:altus:environments:us-west-1:27c485f2-d664-4a62-911c-8454d5ea311a:environment:marccdp/5b56f5d8-6089-43f6-96bb-fa67e9d3ba44 is not a valid CDP Environment crn',)
#seems related to the fact that https://github.com/cloudera-labs/cdpy/blob/main/src/cdpy/dw.py expect 
#a string starting with 
#crn:cdp:environments instead of
#crn:altus:environments




