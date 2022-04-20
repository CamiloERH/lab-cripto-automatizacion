from cProfile import run
import threading
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time
from termcolor import colored


def run_request(email, password):
    url = "https://firstjob.me/usuarios/registro"
    payload='authenticity_token=aK9H%2F95Ks3HRrnwXYCj0tIy0qlqggtvMWCseCIrdugdFJjlGfLSNlA%2BgRG59IHqzKF%2BJdep9u0mYpiqUXFyLjg%3D%3D&user%5Bemail%5D='+email+'&user%5Bpassword%5D='+password+'&user%5Bpassword_confirmation%5D='+password+'&user%5Bterms%5D=0&user%5Bterms%5D=1'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'es-419,es;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_ga=GA1.2.1802248680.1649303822; _gid=GA1.2.887694695.1650425969; _firstjob_v2_session=5GSOnj3F3jmtKZoUBuDLF3Zc7QNAnqwtPAtQbxVVVgxSp4BbhJJiy%2FymBec2UIQ%2FOjz9RzSjW7esmIXeCl5BZStzASLmiIy7n4FNWOZwhNXHsdvBSTLh2UujDqr5MvkujdAF%2Fut5X3SnisL4I7Ey4gT3zR%2FOjIsTT4u3ZtJoNs9KsBT8HDmiYCYEAV6sCwjRceBRcA06YlzezTLzfCAkKEyvM%2Bebt%2FxJXtrP5rZ8BmvuYVaU3F4Yk1u9KPVWcuceycNh%2BBqYA7jvU9EbE2b0oG%2BO61vbbXKl%2FN%2B%2Btw%3D%3D--XfyI0LLp1G6T1%2FKZ--BkanK%2FxNXMRzS5k20weMvg%3D%3D; _firstjob_v2_session=1OOVhPUC4rJ9O7X31PGeyXOy2YFpetYvjBWVyPYdP%2BQuErjZJQI6I0QVjYGfRYB%2F1WUpR2EnxkGH2khJzLjHkLo7LLtHGJEQeaIVheZhXzC1cmCBAohq%2BSUoCjPaFzqTay2yNWgmuBrXQcHw%2BUvxjkXgk1V4rB355zQ72gH%2BOyaPef9USmrWUMrjuNl8xej25g2Ud3canX%2FBotAB8JyBqGhol1y8UjWZhmy77w0phy9L9Wv7F%2F%2FG7tJ4nJn79XpNetE43SIHQIGkgFDBYKrPJ0rrh%2Bwr55SWiXTGOg%3D%3D--3mMm9bvNnztHCK9A--5MWsrIGh6h3TyjKczG7n%2BA%3D%3D',
        'Origin': 'https://firstjob.me',
        'Referer': 'https://firstjob.me/usuarios/registro/nueva_cuenta',
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
    if(response.text.split("\n")[79].strip() == '<p>Tu cuenta ha sido creada con éxito, ahora solo debes confirmarla. Revisa tu correo.</p>'):
        print(colored('Registro exitoso', 'green'))
    else: 
        print(colored('WTF', 'red'))

def main():
    run_request(input('Email: '), input('Password: '))


if __name__ == '__main__':
    main()
