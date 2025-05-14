import urllib.parse
def generate_link(user):
    encoded_username = urllib.parse.quote(user)
    return f"http://www.codewars.com/users/{encoded_username}"