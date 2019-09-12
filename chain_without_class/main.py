#encoding=utf-8

def create_node(data = None, next = None):
	return {'data' : data, 'next' : next}

def set_next_node(cur_node, next_node):
	cur_node['next'] = next_node

# 顺便实现获取下一个节点的函数
def get_next_node(cur_node):
	return cur_node['next']

def create_chain():
	entry = create_node() # 默认 data 是 None，所以不填参数也可以
	# 为了方便，我们为 entry 增加一个 length 字段，保存链表的长度，刚开始是 0
	entry['length'] = 0
	return entry

# 获取链表长度
def get_chain_length(entry):
	return entry['length']

# 链表是否为空
def is_chain_empty(entry):
	return get_chain_length(entry) == 0

# 获取节点数据
def get_node_data(node):
	return node['data']

# 向链表增加数据
def push_chain(entry, data):
	new_node = create_node(data)
	# 为清晰，我们单独把第一个节点保存在 first_node 
	first_node = get_next_node(entry)
	set_next_node(new_node, first_node)
	set_next_node(entry, new_node)

	# 别忘了增加链表节点计数
	entry['length'] += 1

# 从链表头部弹出数据
def pop_chain(entry):
	if is_chain_empty(entry):
		return None

	head = entry
	first_node = get_next_node(head)
	second_node = get_next_node(first_node)
	set_next_node(entry, second_node)
	set_next_node(first_node, None)

	# 切记，更新链表长度
	entry['length'] -= 1

	return first_node['data']


# 遍历链表，便于我们查看链表内容
def chain_all(entry):
	node = entry
	while get_next_node(node):
		node = get_next_node(node)
		print(get_node_data(node))

# 一段简单的测试，
chain = create_chain()

push_chain(chain, "hello")
push_chain(chain, "world")
push_chain(chain, "!")

print("length: {}".format(get_chain_length(chain)))

print("all chain nodes data:")
chain_all(chain)

# 下面是对弹出数据的测试
print("now pop data!")

while not is_chain_empty(chain):

	data = pop_chain(chain)
	print('----pop node data: {}-----'.format(data))
	print('****see the chain nodes ******')
	chain_all(chain)
