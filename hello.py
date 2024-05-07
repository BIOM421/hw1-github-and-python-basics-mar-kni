def hello_world():
	return "Hello World!"
def hello_world_n(N):
	return "Hello World! "*(N-1) + "Hello World!"
print(hello_world_n(4))