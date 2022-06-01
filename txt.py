
# import package
import africastalking

# Initialize SDK
username = "vax"    # use 'sandbox' for development in the test environment
api_key = "627ec15b8423b66494193f75466c00997afb091cfe06e4a081a1dc95b151f544"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello Mercy!", ["+254713303092"])
print(response)