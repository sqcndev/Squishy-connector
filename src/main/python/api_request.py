import requests
import logging

logging.getLogger(__name__)

squishy_download_url = 'https://github.com/squishychain/squishy/releases/download/'
app_release_url = 'https://github.com/squishychain/squishy-connector/releases/'
squishy_api_url = "https://api.github.com/repos/squishychain/squishy/releases/latest"
app_api_url = "https://api.github.com/repos/squishychain/squishy-connector/releases/latest"

coinpaprika = {'market': 'https://api.coinpaprika.com/v1/coins/sqcn-squishy-credit-loops/markets?quotes=USD,TRY,BTC,EUR,RUB',
               'tickers': 'https://api.coinpaprika.com/v1/tickers/sqcn-squishy-credit-loops?quotes=',
               'fiatlist': ['USD', 'TRY', 'BTC', 'EUR', 'RUB']}
exchange_market_api_list = {'coinpaprika': coinpaprika}
"""
requests to get the latest releases' tag_name of a git api url
"""


def git_request_tag(api_url):
    try:
        response = requests.get(api_url, timeout=5)
        tag_name = response.json()["tag_name"]
        return tag_name
    except Exception as e:
        return e


"""
combines the squishy latest download_url with latest releases' tag name to form the latest download url
"""


def latest_squishy_download_url():
    tag_name = git_request_tag(squishy_api_url)
    if type(tag_name) == str:
        latest_download_url = squishy_download_url + tag_name
        return latest_download_url
    else:
        return 'Connection Error'


"""
combines the app's latest release url with latest releases' tag name to form the latest release url
"""


def latest_app_release_url():
    tag_name = git_request_tag(app_api_url)
    if type(tag_name) == str:
        latest_release_url = app_release_url + tag_name
        return latest_release_url
    else:
        return 'Connection Error'


def get_squishy_stats():
    try:
        response = requests.get('https://explorer.squishy.io/insight-api-komodo/stats', timeout=5)
        return response.json()
    except Exception:
        try:
            response = requests.get('https://explorer2.squishy.io/insight-api-komodo/stats', timeout=5)
            return response.json()
        except Exception:
            try:
                response = requests.get('https://explorer3.squishy.io/insight-api-komodo/stats', timeout=5)
                return response.json()
            except Exception as e:
                logging.error(e)
                return 'error'


def sqcn_exchange_market(api_list_key):
    api_url_list = exchange_market_api_list.get(api_list_key)
    response_list = []
    tickers_list = {}
    try:
        response = requests.get(api_url_list.get('market'), timeout=5)
        response_list.append(response.json())
    except Exception as e:
        logging.error(e)
        response_list.append('error')

    for app_api_url in api_url_list.get('fiatlist'):
        app_api_url = api_url_list.get('tickers') + app_api_url
        try:
            response = requests.get(app_api_url, timeout=5)
            tickers_list.update(response.json().get('quotes'))
        except Exception as e:
            logging.error(e)
            response_list.append('error')
    response_list.append(tickers_list)
    return response_list


def get_blocks_details(block, hash):
    api_url_list = ['https://explorer.squishy.io/insight-api-komodo/blocks',
                    'https://explorer2.squishy.io/insight-api-komodo/blocks',
                    'https://explorer3.squishy.io/insight-api-komodo/blocks']
    result_lists = []
    for api_url in api_url_list:
        try:
            response_e = requests.get(api_url, timeout=15)
            response_json = response_e.json().get('blocks')
            block_e = None
            hash_e = None
            previous_hash_e = None
            for item in response_json:
                index = response_json.index(item)
                if int(item.get('height')) == int(block) and item.get('isMainChain') == True:
                    block_e = item.get('height')
                    hash_e = item.get('hash')
                    previous_hash_e = response_json[index+1].get('hash')
                    break
            if block_e is None and hash_e is None and previous_hash_e is None:
                api_index = api_url_list.index(api_url)
                hash_response = get_block_hash(hash, api_index)
                block_e = block
                hash_e = hash_response.get('hash')
                previous_hash_e = hash_response.get('previousblockhash')
            result_list = []
            if block_e:
                result_list.append(block_e)
            if hash_e:
                result_list.append(hash_e)
            if previous_hash_e:
                result_list.append(previous_hash_e)
        except Exception:
            result_list = []
        if result_list:
            result_lists.append(result_list)
    if result_lists:
        return result_lists
    else:
        return 'error'


def get_block_hash(hash, index):
    api_url_list = ['https://explorer.squishy.io/insight-api-komodo/block/' + hash,
                    'https://explorer2.squishy.io/insight-api-komodo/block/' + hash,
                    'https://explorer3.squishy.io/insight-api-komodo/block/' + hash]
    try:
        response_e = requests.get(api_url_list[index], timeout=15)
        return response_e.json()
    except Exception:
        return

