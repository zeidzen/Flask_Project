
email = """Hi Jane,

Thank you for keeping me updated on this issue. I'm happy to hear that the issue got resolved after all and you can now use the app in its full functionality again. 
Also many thanks for your suggestions. We hope to improve this feature in the future. 

In case you experience any further problems with the app, please don't hesitate to contact me again.

Best regards,

John Doe
Customer Support

1600 Amphitheatre Parkway
Mountain View, CA
United States """

from talon.signature.bruteforce import extract_signature
cleaned_email, _ = extract_signature(email)
print (cleaned_email)
lines = cleaned_email.split('\n')
lines = [line for line in lines if line != '']
cleaned_email = ' '.join(lines)

print ('=='*30)
print (cleaned_email)