import pyshorteners

url = input("Enter the URL you want to shorten: ")

# Create a Shortener object with the desired URL shortening service
shortener = pyshorteners.Shortener()

# Shorten the URL using the Shortener object
short_url = shortener.tinyurl.short(url)

# Print the shortened URL
print("Short URL:", short_url)