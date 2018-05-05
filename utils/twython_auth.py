from twython import Twython

print('Go to https://apps.twitter.com/ and create an API key')

api_key = input('Enter your API key: ')
api_secret = input('Enter your API secret:')

twitter = Twython(api_key, api_secret)

auth = twitter.get_authentication_tokens()
print(auth['oauth_token'])
print(auth['oauth_token_secret'])
print(auth['auth_url'])
oauth_verifier = input('Enter your pin:')
twitter = Twython(api_key,
                  api_secret,
                  auth['oauth_token'],
                  auth['oauth_token_secret'])
final_step = twitter.get_authorized_tokens(oauth_verifier)
print('export TWITTER_APP_KEY="{api_key}"'.format(api_key=api_key))
print('export TWITTER_APP_SECRET="{api_secret}"'.format(api_secret=api_secret))
print('export TWITTER_OAUTH_TOKEN="{oauth_token}"'.format(oauth_token=final_step['oauth_token']))
print('export TWITTER_OAUTH_TOKEN_SECRET="{oauth_token_secret}"'.format(oauth_token_secret=final_step['oauth_token_secret']))
