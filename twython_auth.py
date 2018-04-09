from twython import Twython

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
print('oauth_token', final_step['oauth_token'])
print('oauth_token_secret', final_step['oauth_token_secret'])
