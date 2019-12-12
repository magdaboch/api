SERVER = {
    'url': 'https://jsonplaceholder.typicode.com'
}

# FULL_ROUTE = '{url}/{path}/{version}'.format(
#     url = SERVER['url'],
#     path = SERVER['path'],
#     version = SERVER['version']
# )

FULL_ROUTE = '{url}'.format(**SERVER)


if __name__ == '__main__':
    print(FULL_ROUTE)