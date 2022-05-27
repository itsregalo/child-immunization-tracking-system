
# import package
import africastalking

# Initialize SDK
username = "mercyk"    # use 'sandbox' for development in the test environment
api_key = "f974401965cacf2e18ce7ff1784a1d062723a716f2021793dad3834e21070dda"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello Message!", ["+254713303092"])
print(response)