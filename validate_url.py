
import re

def validate_url(url):
    pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return pattern.match(url) is not None


def main():
    urls = [
        "http://example.com",
        "https://www.example.com/path",
        "ftp://example.com",
        "http://localhost:8080",
        "not-a-url"
    ]
    for url in urls:
        print(f"'{url}' -> {validate_url(url)}")


if __name__ == "__main__":
    main()
