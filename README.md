# SparkClearYourMsgs
This python script lets you clear your messages out of a Spark room / space. 

1) Log into https://developer.ciscospark.com/ with your spark credentials 

2) Go to one of the API test pages. Like: https://developer.ciscospark.com/endpoint-messages-get.html

3) Near the top right half of the screen there will be a "Test Mode" toggle. Turn it to "ON". 

4) Record the Authorization code, or Access Token. 

5) Open web.ciscospark.com and log in if your aren't already. 

6) Navigate to the room in wich you want to clear messages from. 

7) In the URL you'll want to find the Room ID as depicted with X's in this example: https://web.ciscospark.com/rooms/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/chat

8) Run the script and you will be asked for your e-mail (your e-mail and it is case sensitive), the access token, the room ID, and finally the max number of messages you want to retrieve. 

9) The script will run and grab the max number of messages from the room and delete the ones that belong to you. 

10) Profit.    

# SparkClearYourMsgs
