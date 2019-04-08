import socket
import sys
import requests
import requests_oauthlib
import json

CONSUMER_KEY = '7BqOGU3L2fa9c4zN3MLswu7l1'
CONSUMER_SECRET = 'hDTne3k80xoYhZA37nBgpkG9jkvwL8JT4iBnrJeiL7KNMWizOA'
ACCESS_TOKEN = '237109800-71pu0HOngTrF9UeVDorBnkD4r4EdpvdYZMTxyDkG'
ACCESS_SECRET = 'tD64Mr9kQspQBjlka89igUdSd74Bvvek5xXve3fAvnh46'
my_auth = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET)





#Now, we will create a new function called get_tweets that will call the Twitter API URL and return the response for a stream of tweets.


def get_tweets():
	url = 'https://stream.twitter.com/1.1/statuses/filter.json'
	query_data = [('language', 'en'), ('locations', '-130,-20,100,50'),('track','#')]
	query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
	response = requests.get(query_url, auth=my_auth, stream=True)
	print(query_url, response)
	return response


#Then, create a function that takes the response from the above one and extracts the tweets’ text from the whole tweets’ JSON object. After that, it sends every tweet to Spark Streaming instance through a TCP connection.

def send_tweets_to_spark(http_resp, tcp_connection):

	for line in http_resp.iter_lines():
		try:
			print (line)
			full_tweet = json.loads(line.decode('utf-8'))
			tweet_text = full_tweet['text']+'\n'
			print("Tweet Text: " + tweet_text)
			print ("------------------------------------------")
			
			
			tcp_connection.send(tweet_text.encode('utf-8'))
		except Exception as e:
			e = sys.exc_info()[0]
			print("Error: %s" % e)



#Now, we’ll make the main part which will make the app host socket connections that spark will connect with. We’ll configure the IP here to be localhost as all will run on the same machine and the port 9009. Then we’ll call the get_tweets method, which we made above, for getting the tweets from Twitter and pass its response along with the socket connection to send_tweets_to_spark for sending the tweets to Spark




TCP_IP = "localhost"
TCP_PORT = 9009
conn = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Waiting for TCP connection...")
conn, addr = s.accept()
print("Connected... Starting getting tweets.")
resp = get_tweets()
send_tweets_to_spark(resp, conn)



