from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

credential = DefaultAzureCredential()
subscription_id = 'Azure-Subscription'
client = ResourceManagementClient(credential,subscription_id)

resource_groups = client.resource_groups.list()

for rg in resource_groups:
    print(rg.name)