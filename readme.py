############### this is not a real readme this just took up way too much space in my script file i swear im not an animal im couth ... ###############

# to activate environment: source venv/bin/activate

## goal: find all space emails from alice (and the others). to simply find alice, comment out lines 9, 31, 32. uncomment lines 8 and 30
## steps:
# 1. pull message list
# 2. parse for message id
# 3. call view.php with that id
# 4. pull html message body from JSON array

## how the data works - POST requests
# 1. refresh button: https://space.galaxybuster.net/lib/get.php (html)
#   <div data id> 
#       <span>from</span>
#       <span>to</span>
#   </div> 
# 2. view message: https://space.galaxybuster.net/lib/view.php (JSON array)
#   [0] - html message (msgSubject, msgSender, msgBody, msgDate)
#   [1] - random id
#   [2] - "not signed in