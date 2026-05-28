import base64

code_str = "cGlwZWxpbmUgewogICAgYWdlbnQgYW55CgogICAgdG9vbHMgewogICAgICAg\nIGpkayAnamRrMTcnCiAgICAgICAgbWF2ZW4gJ01hdmVuMycKICAgIH0KCiAg\nICBzdGFnZXMgeyAgIAogICAgICAgIHN0YWdlKCdDb21waWxlJykgewogICAg\nICAgICAgICBzdGVwcyB7CiAgICAgICAgICAgICAgICBzaCAnbXZuIGNvbXBp\nbGUnCiAgICAgICAgICAgIH0KICAgICAgICB9CiAgICAgICAgCgogICAgICAg\nIAogICAgICAgIHN0YWdlKCdCdWlsZCcpIHsKICAgICAgICAgICAgc3RlcHMg\newogICAgICAgICAgICAgICAgc2ggJ212biBwYWNrYWdlJwogICAgICAgICAg\nICB9CiAgICAgICAgfQogICAgfQp9Cg==\n"

print(base64.b64decode(code_str).decode())
from urllib.parse import urlparse



def get_owner_and_repo(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip("/")

    print(path_parts)
    if len(path_parts) >= 2:
        owner, repo = path_parts[0], path_parts[1]
        return owner, repo
    return None, None

get_owner_and_repo("https://api.github.com/happy111/Boardgame/")