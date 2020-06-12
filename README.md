# ebayapi2.py is the latest version that uses eBay API to get results based on entries in ebay_search.txt file
I realised that I used https://github.com/DrPi101/webscrape-rm/blob/master/ebayapitest.py in the video on YouTube

# https://youtu.be/iJy1U9Xik2w



1. Create a file called ebayapi.py (make sure it is in same directory as your python code)

2 Inside that file put the following on one single line:
ebayapi = 'mrBlobby-ebpyt-PRD-dcaa423c9-9a37ab99'
where mrBlobby is the usename (I haven't put my own personal one here for obvious reasons).

3. With that file saved, you can then use "ebayapi"  on line 14 - eg.  appid = ebayapi
full line reads : 

api = finding(appid = ebayapi, siteid='EBAY-GB', config_file=None) # change country with 'siteid='

See my working code on GitHub : 
https://github.com/DrPi101/webscrape-rm/blob/master/ebayapitest.py
https://github.com/DrPi101/webscrape-rm/blob/master/ebay_search.txt 
(the txt file is the list of things to search for that the Python code reads).

4. Note I am using the PRD production key that gets data from the 'Live' eBay site.
5. See also https://developer.ebay.com/DevZone/building-blocks/eBB_Join.pdf
6. To do what I've shown in the video, you just need: appid

If you hover over the link on the page : https://developer.ebay.com/my/keys
You can see more info:

"Now that you have an App ID, you can:

    Use the App ID as your credentials to make Finding API calls in the selected environment.
    If an eBay member wants to use your application to create listings, manage orders, etc., you'll need to generate a User Token for them."
