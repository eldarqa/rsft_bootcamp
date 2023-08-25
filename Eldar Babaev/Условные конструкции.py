def normalize_url(url):
    if url[:7] == 'http://':
        return 'https' + url[4:]
    if url[:8] == 'https://':
        return url
    else:
        return 'https://' + url