import requests


def downloader(url, chunk_size):
    response = requests.get(url, stream=True)
    iter_content = response.iter_content(chunk_size)
    for value in iter_content:
        yield value
