import requests


def parse_nginx_log():
    url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    content = requests.get(url=url)
    with open('logs.txt', 'w', encoding='utf-8') as f:
        f.write(content.text)

    list_logs = []

    with open('logs.txt', 'r', encoding='utf-8') as f:
        for i in f:
            step = f.readline()
            if step is not None:
                logs_tuple = (step.split()[0], step.split()[5][1:], step.split()[6])
                list_logs.append(logs_tuple)
    print(list_logs)


parse_nginx_log()