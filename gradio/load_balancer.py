```python 
class Server:
    def __init__(self, server_id, capacity):
        self.server_id = server_id 
        self.capacity = capacity 
        self.current_requests = 0 
 
    def can_handle_request(self):
        return self.current_requests < self.capacity 
 
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers 
 
    def get_next_server(self):
        for server in self.servers:
            if server.can_handle_request():
                server.current_requests += 1 
                return server 
 
        raise Exception("All servers are busy")
 
# 创建一些服务器 
server1 = Server(1, 2)
server2 = Server(2, 3)
server3 = Server(3, 1)
 
# 创建负载均衡器 
lb = LoadBalancer([server1, server2, server3])
 
# 分发请求 
for i in range(10):
    server = lb.get_next_server()
    print(f"Request {i+1} sent to server {server.server_id}")
