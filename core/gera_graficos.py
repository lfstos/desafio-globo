import requests


def _consumo_cpu():
    response = requests.get('https://run.mocky.io/v3/b1bc5162-7cf2-4599-b1f5-e3bd58fcf07f')
    resp = response.json()

    data = {
        'labels': resp['labels'],
        'values': resp['data']
    }

    return data


def _consumo_memoria():
    response = requests.get('https://run.mocky.io/v3/d23c3262-967e-4567-b7f6-2fd263748811')
    resp = response.json()

    data = {
        'labels': resp['labels'],
        'values': resp['data']
    }

    return data


def _info_cluster(request):
    response = requests.get('https://run.mocky.io/v3/cab2791c-7c85-4461-b95c-86bc1a12dc72')
    resp = response.json()

    data = {
        'labels': resp['status'],
        'values': resp['status']
    }

    return data
