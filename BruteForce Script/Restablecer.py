from termcolor import colored
from cProfile import run
import threading
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def run_request(email):
    url = "https://firstjob.me/usuarios/recuperar_acceso"
    payload = 'authenticity_token=bNvnSSiXhxrYanUkoDRCy9yJt8jqeKA%2F%2BeFU5T5ovn9BUpnwimm5%2FwZkTV29PMzMeGKU56CHwLo5bGB56OmP9g%3D%3D&user%5Bemail%5D='+email
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'es-419,es;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_ga=GA1.2.1802248680.1649303822; _gid=GA1.2.887694695.1650425969; _firstjob_v2_session=4v0TRNoFDsqWETbRm7wvh0Or9QCgiX6LrU0zFZ2q4qANmQJGPHkBQcqV%2BBRR3nxR6Ern82MnYhS5zfT%2F%2Bqjee%2FrT%2FWU8Ak1dUVKvA934pX7fQK%2F2xx%2FD57%2Bo%2Fv6rmywWIi3fpPAmDGUhLE0ukBsT1mlDLEhQ%2FW%2FNK%2F8x50td%2FUjU%2B%2B4iHfe%2B1%2F%2FLccosMX2TcCPH2G%2BwCdijo1ukoegt8grwKc0BfIjz3gfH0yzW96C4YKnNdCOBKM9rQ9aOsgPHx7tcB%2FzJMsqiVv0PHU%2FQK7N6gYp3doLAZ2XQaA%3D%3D--QmaQcya5PFOWex7U--GJa12U9I1zbbsiX8CrBSoQ%3D%3D; _gat_gtag_UA_164980910_2=1; _firstjob_v2_session=hmozNqVab05cA%2FZeypZ%2B3KtPTjsoZTW7VUaoJ6MXGFLNKOFT2bcrBDGStSRLCUBoEIZbyYkfsJeyXTGw6KjDs3FOdNGwnKDI1AAV%2BRH5P9Np33BjiqU0tFHBIxAm41NC8gq2zcaPYlHsJV2SSmGGwh3QvKHgLOoptLBcYsPYzOHJBfzxAQchzdqqFVrV%2FgghD%2BqRUsRGaGW6HfgNfllAzgy5xJtyAl0EsSzps0vEQXkPCamiRl6cwoVnMOA7rtyvsYOgWchgmKLXh%2F0VKers3omagWrZGur%2BQGINDQ%3D%3D--BKcqSTgwanidcTB1--4U3a1pFCvai7%2Bu4GI%2BMY9Q%3D%3D',
        'Origin': 'https://firstjob.me',
        'Referer': 'https://firstjob.me/usuarios/recuperar_acceso/new',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print(colored(response.text.split("\n")[81].strip(), 'green'))


def main():
    print('Recuperar password ingrese Email: ')
    run_request(input('Email: '))


if __name__ == '__main__':
    main()
