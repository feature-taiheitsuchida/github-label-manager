import argparse
import requests

parser = argparse.ArgumentParser(description='test description')
parser.add_argument('--oauth_token', type=str, help="github's oauth token.")
parser.add_argument('--owner', type=str, help="github's oauth token.")
parser.add_argument('--repos', type=str, help="github's oauth token.")
args = parser.parse_args()
print(type(args.oauth_token))
print(args.oauth_token)

header = {
    'Authorization': args.oauth_token
}
url = f"https://api.github.com/repos/#{args.owner}/#{args.repos}/labels"
requests.get(url, header)
