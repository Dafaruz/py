from twilio.rest import Client

account_sid = '[]'
auth_token = '[]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16123516006',
  body='HI HUYS',
  to='+9720548318600'
)

print(message.sid)
