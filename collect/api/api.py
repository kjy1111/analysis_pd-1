# PD API Wrapper Functions
import math
from datetime import datetime
from urllib.parse import urlencode
from .web_request import json_request


def pd_gen_url(endpoint, service_key, **param):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(param), service_key)
    return url


def pd_fetch_foreign_visitor(country_code, year, month, service_key=''):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    url = pd_gen_url(
        endpoint,
        service_key,
        YM='{0:04d}{1:02d}'.format(year, month),
        NAT_CD=country_code,
        ED_CD='E',
        _type='json')
    json_result = json_request(url=url)

    json_response = json_result.get('response')
    json_header = json_response.get('header')
    result_message = json_header.get('resultMsg')
    if 'OK' != result_message:
        print('%s Error[%s] for request %s' % (datetime.now(), result_message, url))
        return None

    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None


def pd_fetch_tourspot_visitor(
        district1='',
        district2='',
        tourspot='',
        year=0,
        month=0,
        service_key=''):

    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    pageno = 1
    hasnext = True

    while hasnext:
        url = pd_gen_url(
            endpoint,
            service_key,
            YM='{0:04d}{1:02d}'.format(year, month),
            SIDO=district1,
            GUNGU=district2,
            RES_NM=tourspot,
            numOfRows=100,
            _type='json',
            pageNo=pageno)
        json_result = json_request(url=url)
        if json_result is None:
            break

        json_response = json_result.get('response')
        json_header = json_response.get('header')
        result_message = json_header.get('resultMsg')

        if 'OK' != result_message:
            print('%s : Error[%s] for Request(%s)' % (datetime.now(), result_message, url), file=sys.stderr)
            break

        json_body = json_response.get('body')

        numofrows = json_body.get('numOfRows')
        totalcount = json_body.get('totalCount')

        if totalcount == 0:
            break

        last_pageno = math.ceil(totalcount/numofrows)
        if pageno == last_pageno:
            hasnext = False
        else:
            pageno += 1

        json_items = json_body.get('items')
        yield json_items.get('item') if isinstance(json_items, dict) else None