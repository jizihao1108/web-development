from twilio.rest import TwilioRestClient

account_sid = "AC7368c8844f34d1d1a15eb1cbd18fc9c2" # Your Account SID from www.twilio.com/console
auth_token  = "bc20c4307285bc67306bb939fce6aa0a"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body='Yo, fuck you',
    to="+14046626334",    # Replace with your phone number
    from_="+14157993746") # Replace with your Twilio number

print(message.sid)