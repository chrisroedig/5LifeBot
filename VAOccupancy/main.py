import requests
import re as reg

IFRAME_URL = 'https://portal.rockgympro.com/portal/public/bc4d3be86f2f8564a4e5e4f9151f6bf6/occupancy?iframeid=occupancyCounter&fId=1068'

def handler(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    r = requests.get(IFRAME_URL, verify=False)
    raw_data = r.text.encode('utf-8').decode('unicode_escape')
    data = {
        'count': reg.search("\\\'count\\\' : (.*),", raw_data)[1],
        'capacity': reg.search("\\\'capacity\\\' : (.*),", raw_data)[1]
    }
    greeting = 'Head over and Climb On!'
    if(float(data['count'])/float(data['capacity']) >= 0.75 ):
        greeting = 'Better hurry up, lots of people here.'
    if(float(data['count'])/float(data['capacity']) >= 0.95 ):
        greeting = '🤬 The gym is full.'
    
    return {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f'{greeting}',
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'There are *{data["count"]}* people climbing right now.'
                }
            },
            {
		"type": "context",
		"elements": [
			{
				"type": "plain_text",
				"text": f'Pulled from VA website. Max capacity is {data["count"]}',
				"emoji": True
			}
		]
	    }
        ]
    }
