from funciones.generate_user_agent import generate_user_agent
import urllib.request
from bs4 import BeautifulSoup
def check_url(url):
    result = {'title': '', 'link': url}
    try:
        user_agent = generate_user_agent()
        headers = {'User-Agent': user_agent}
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=10) as connection:
            code = connection.getcode()
            if code == 200:
                content = connection.read()
                soup = BeautifulSoup(content, 'html.parser')
                title_tag = soup.find('title')
                if title_tag:
                    title = title_tag.text.strip()
                    result['title'] = title
                    print(f'[Éxito] URL verificada: {url}, Titulo: {title}')
    except Exception as e:
        print(f'[Fallo] Verificación de la URL {url}: {str(e)}')
    return result