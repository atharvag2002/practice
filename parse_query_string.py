
def parse_query_string(query):
    parts = query.split('&')
    return dict(part.split('=') for part in parts if '=' in part)


def main():
    print(parse_query_string('a=1&b=2'))

if __name__ == "__main__":
    main()
