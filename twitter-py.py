import twitter
from bintrees import FastBinaryTree
from time import sleep


tree = FastBinaryTree()
keys = [ TOKENS ]


def get_token():
	token = keys.pop()
	keys.insert(0, token)
	return twitter.Api(token[0], token[1], token[2], token[3])


def BFS(api, node):
	count, error = 0, 0
	queue = [node.id]
	tree.insert(node.screen_name, node.id)
	with open('amigos.txt', 'w') as file:
		while queue and count < 100:
			u = queue.pop(0)
			try:
				friends = [(i.screen_name, i.id) for i in api.GetFriends(user_id=u, total_count=5)]
			except twitter.error.TwitterError:
				queue.insert(0, u)
				error += 1
				if error == len(keys):
					sleep(900)  # 15 min
					error = 0
				api = get_token()
			else:
				count += 1
				for friend in friends:
					if not tree.get(friend[0]):
						tree.insert(friend[0], friend[1])
						queue.append(friend[1])
					file.write('{0} -> {1}\n'.format(u, friend[1]))


if __name__ == '__main__':
	api = get_token()
	if api:
		me = api.GetUser(screen_name="kaioduarteds")
		BFS(api, me)
