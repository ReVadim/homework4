from application.md5_convert import md5_convert


def text_read(file_path):
    for row in open(file_path, 'r', encoding='utf-8'):
        yield md5_convert(row.rstrip('\n'))
