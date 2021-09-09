def get_notes(url, section):
    '''
    Function that returns a URL list to the notes in a section
    '''
    featured_article = section.find('section', attrs={'class': "top-content"})

    featured_link = url + \
        featured_article.a.get('href') if featured_article else None

    article_list = section.find_all(
        'h4', attrs={'class': "is-display-inline title-list"})

    if featured_link:
        return [featured_link] + [f"{url}{article.a.get('href')}" for article in article_list if article]

    return [f"{url}{article.a.get('href')}" for article in article_list if article]


def get_info(soup_note):
    info = {
        'title': None,
        'teaser': None,
        'subheader': None,
        'author': None,
        'body':}

    title = soup_note.find('div', attrs={'class': "col 2-col"}).find('h1')
    if title:
        info['title'] = title

    # volanta
    teaser = soup_note.find(
        'div', attrs={'class': "col 2-col"}).find('h4')  # maybe None

    # copete o bajada
    subheader = soup_note.find(
        'div', attrs={'class': "col 2-col"}).find('h3')  # maybe None

    # author
    author = soup_note.find('div', attrs={'class': "author-name"})

    # cuerpo
    body = soup_note.find(
        'div', attrs={'class': "article-main-content article-text"}).find_all('p')
    body_text = [b.text for b in body]
