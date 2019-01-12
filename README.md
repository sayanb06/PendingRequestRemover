# PendingRequestRemover
A bot to go through each outgoing friend request and cancel the request


## How To Use
1. Download Selenium for python >= 2.7 using `pip install selenium`
2. Download [Chrome WebDriver](https://chromedriver.storage.googleapis.com/index.html?path=2.45/) and unzip and place the application in the same folder as the script
3. Make a "facebook.txt" file containing the following things in order on different lines:
    1. Email
    2. Password
    3. An upper bound of the number of outgoing friend requests you have (just put a large number if unknown)
4. Run the script using `python removeRequests.py  `

## Inspiration
I wanted to get an introduction to bots. Clearing up many friend requests could have taken a long time and I thought this would be a perfect way to learn.