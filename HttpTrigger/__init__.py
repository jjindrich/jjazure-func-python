import logging

import azure.functions as func
import requests

''' sample pro test
{
    "name" :"Call azure server",
    "url": "http://jjdevv2addc.jjdev.local"
}
{
    "name" :"Call azure server",
    "url": "http://jjdevv2appw.jjdev.local"
}
{
    "name" :"Call onprem server",
    "url": "http://jjdevbr1web.jjdev.local"
}
'''

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    adresa = req.params.get('url')
    if not adresa:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            adresa = req_body.get('url')

    logging.info("JJ log")

    if not adresa:
            adresa = "http://www.google.com"

    logging.info(adresa)
    r = requests.get(adresa)
    logging.info(r.content)
    name = r.content


    logging.info("JJ log finished")

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
