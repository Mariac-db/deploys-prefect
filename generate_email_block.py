from prefect_email import EmailServerCredentials
from mail_credentials import gmail, pssw

credentials = EmailServerCredentials(
    username = gmail,
    password = pssw ,  # must be an app password por si las moscas 
)
credentials.save("email-creds")

# to read it 
# from prefect_email import EmailServerCredentials
# EmailServerCredentials.load("email-creds")
