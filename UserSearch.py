from googleapi import google

def search_user(query):

    num_pages = 3
    searchResults = google.search(query, num_pages)
    return searchResults
