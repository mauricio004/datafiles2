__author__ = 'MFlores1'


from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACee882710d9f5a17aecb5455bdbefe054"
auth_token  = "1686dd721550eae1a1143e3fad3edd3f"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello, are you there?",
    to="+19253017046",    # Replace with your phone number
    from_="+14152369774")  # Replace with your Twilio number
print message.sid