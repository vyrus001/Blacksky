from atproto import Client
import getpass
import sys

if len(sys.argv) < 2: print(f'usage: python <{sys.argv[0]}> <username>'); exit(1)
actor = sys.argv[1]

client = Client()
client.login(actor, getpass.getpass())

currentCursor = None
print('\033[1;37mremoving posts...')
while True:
    resp = client.get_author_feed(actor, cursor=currentCursor)
    currentCursor = resp.cursor

    for feedViewPost in resp.feed:
        print(f'\033[0;35m->\t{feedViewPost.post.record.text}')
        if not client.delete_post(feedViewPost.post.uri):
            print(f'\033[91m[*]failed to remove post -> {feedViewPost.post.uri}')
            exit(1)
                
    if currentCursor is None: print('\033[1;37m', end=''); break

print('Done!')
