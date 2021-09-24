import requests

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