# Tarot Reader
A twitter bot to provide tarot readings!

This python3 program uses tweepy and pycorpora to create tarot readings.

## Build Docker Image to Test
 1. Run the command in the bash shell from the project directory:

     ```docker build . -t tarot-reader-bot```

 2. Test your build from powershell with
   
     ```docker run -it -e CONSUMER_KEY=$TarotConsumer -e CONSUMER_SECRET=$TarotConsumerSecret -e ACCESS_TOKEN=$TarotAccess -e ACCESS_TOKEN_SECRET=$TarotAccessSecret tarot-reader-bot```

## Build and Deploy Docker Image
Note: Everything is in the bash shell for this part! This is also for digital ocean droplets, and `twitter-bot-drop` is the name of my digital ocean droplet that I'm making and `tarot-reader-bot` is the docker image name.
1. If you don't have anything registered as a docker-machine (which controls multiple instances of docker images) then you make one.
   
    ```docker-machine create --driver digitalocean --digitalocean-access-token YOUR-ACCESS-TOKEN-HERE twitter-bot-drop```

2. Then this command sets your current shell environment to be your docker-machine shell environment
   
    `eval $(docker-machine env twitter-bot-drop)`

3. Then in your new shell you build your docker image
   
    `docker build . -t tarot-reader-bot`

4. And then deploy it! The only difference here is the -id instead of -it which just tells it you want it to be detached from your shell.
   
    `docker run -id -e CONSUMER_KEY=$TarotConsumer -e CONSUMER_SECRET=$TarotConsumerSecret -e ACCESS_TOKEN=$TarotAccess -e ACCESS_TOKEN_SECRET=$TarotAccessSecret tarot-reader-bot`

Et voila! Functioning docker image running on your droplet (which is called a docker-machine)

## References
- [Corpora Library](https://github.com/dariusk/corpora)
- [PyCorpora package](https://github.com/aparrish/pycorpora)