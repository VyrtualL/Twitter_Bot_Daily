# Twitter_Bot_Daily

Hello, here a Daily Bot for Twitter, which will post 1 image per 4 hours

Here what you have to do to use this bot :

First : Install Python3 in your Desktop (I think it's obvious)

Second : Create a Twitter Dev account on this link : https://developer.twitter.com/en

Third : Copy/Paste your account keys and token after these variables :

        consumer_key = 
        consumer_secret =
        access_token = 
        access_token_secret = 
        
Fourth : Rename all your pictures/fanart/draw in this format :
         
         number_between_1_and_1000 or number_between_1_and_1000.jpg
         Exemples : 0001 or 0001.jpg
                    0562 or 0562.jpg
         Warning : you cannot have a number bigger than 999 (not 1000 and 1001 and ,...)
         PS : you can change jpg by other extensions
         
Fifth : Replace the ligne 35 by the path where are your images (use pwd)

        fileName = "/Users/Desktop/Bot/" + a
        Exemples : fileName = "/Windows/username/Desktop/images/" + a

Sixth : It's finish !
