import os


def get_wiki_search():
    url_lookup = input('What wiki page would you like to search today \n> ')

    clean_url = '_'.join(url_lookup.split())

    return clean_url


def error_message():
    print('That is not a valid entry please try again!')


def browser_selection():
    res = input(
        'First which browser would you like to use? \n[A] Chrome \n[B] Edge \n>')

    if res == 'a' or res == 'A':
        return 'Chrome'
    elif res == 'b' or res == 'B':
        return 'Edge'
    else:
        error_message()
        return browser_selection()


def search_function():
    url = get_wiki_search()
    browser = browser_selection()
    chrome_url = "start chrome https://en.wikipedia.org/wiki/" + url
    edge_url = "start msedge https://en.wikipedia.org/wiki/" + url

    if browser == 'Chrome':
        os.system('cmd /c ' + chrome_url)
    elif browser == 'Edge':
        os.system('cmd /c' + edge_url)


search_function()

keep_looking = input('Keep looking? \n[A] Yes \n[B] No \n>')

if keep_looking == 'a' or keep_looking == 'A':
    search_function()
