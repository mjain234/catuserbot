from sample_config import Config


class Development(Config):
  #get this values from the my.telegram.org
  APP_ID = 5908616
  API_HASH = "6502755e902871428b244fc38d9d2ec3"
  # the name to display in your alive message
  ALIVE_NAME = "All Mighty"
  # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
  DB_URI = "postgres://uesrnwfk:x-QBvQ0ipqWunWH9AXuo5gBhBVl3axpo@castor.db.elephantsql.com/uesrnwfk"
  #After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
  STRING_SESSION = "1BVtsOJEBu7lBN_j0E3w2NkbUeXIn9_0o5QUUA4rWXBtzgllcxjQG6Um4LOQwg6IKErHUbOG24_Gqih-n9_ku3b4G53hNWjxALG2fvS2swx0Cl_f6QB9jYYUgy0KwhAVmPqt3laBKM3EI5nfHnbxSUMDUfBXXaeh53rYAdeioqRxOsZJ9kODX1Cw7fF7y7Wt9TP4ENFcjkA58y7xkMupGj_Nge0r0jxWwgxxuXsTXho_xpO3ua7mPaaQriaAZUA8b78GLXWxiFYxCo1fYlZdexACIaMRDl0hznM0S3AIbCweHjV3hQVwdjYFXEqGl2UL3wF94dTJWyl3RaVth3451HnCXa_2iEvk="
  #create a new bot in @botfather and fill the following vales with bottoken and username respectively
  TG_BOT_TOKEN = "5771287936:AAFQ5gBf_HbYrucZjnfpSt6S8ChNJMEeS9s"
  TG_BOT_USERNAME = "@cat96_bot"
  #create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
  PRIVATE_GROUP_BOT_API_ID = -1001739926316
  #command handler 
  COMMAND_HAND_LER = "."
  #sudo enter the id of sudo users userid's in that array
  SUDO_USERS = []
  # command hanler for sudo
  SUDO_COMMAND_HAND_LER = "."
