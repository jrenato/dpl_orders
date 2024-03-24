'''
Mailchimp package testing
'''
import os

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError


try:
    client = MailchimpMarketing.Client()
    client.set_config(
        {
            "api_key": os.environ.get('MC_KEY'),
            "server": os.environ.get('MC_PREFIX'),
        }
    )
    response = client.ping.get()
    if 'health_status' not in response or response['health_status'] != "Everything's Chimpy!":
        raise ValueError(response)

    # Get list of campaigns
    # response = client.campaigns.list()
    # for campaign in response['campaigns']:
    #     print(campaign['id'])

    # Get templates
    test_template_id = None
    response = client.templates.list()
    for template in response['templates']:
        if template['name'] == 'Test Template':
            test_template_id = template['id']
            break

    if not test_template_id:
        raise ValueError('Test template not found')

    # Create campaign
    response = client.campaigns.create(
        {
            "type": "regular",
            # "recipients": {
            #     "list_id": "test",
            # },
            "settings": {
                "subject_line": "Test campaign",
                "title": "Test campaign",
                "template_id": test_template_id,
            },
        }
    )
    print(response)
except ApiClientError as error:
    print(error)
