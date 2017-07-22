#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(shipping-cost-package)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "shipping.price.according.to.box":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("package_types")

    cost = {'envelop 1':38.95, 'box 2':49.95, 'box 3':57.95, 'box 4':78.95, 'box 5':138.95, 'box 6':172.95, 'box 7':199.95}

    speech = "The cost of shipping " + zone + " is " + str(cost[zone]) + " euros."

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
s
