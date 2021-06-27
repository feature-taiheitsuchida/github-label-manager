import argparse
import urllib.request
import ssl


parser = argparse.ArgumentParser(description='test description')
parser.add_argument('--oauth_token', type=str, help="github's oauth token.")
parser.add_argument('--repos', type=str, help="target repos. `{owner}/{repos}`.")
args = parser.parse_args()

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
headers = {
    'Authorization': args.oauth_token
}
url = f"https://api.github.com/repos/{args.repos}/labels"
req = urllib.request.Request(url, headers=headers, method='GET')
print(f"url is {url}.")
with urllib.request.urlopen(req, context=context) as res:
    body = res.read()
print(body)
