from locust import HttpUser, between, task

class MyUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def get_posts(self):
        self.client.get("/posts")
    
    @task
    def get_users(self):
        self.client.get("/users")
    
    @task
    def create_post(self):
        data = {
            "title": "New Post",
            "body": "This is a new post",
            "userId": 1
        }
        headers = {"Content-Type": "application/json"}
        self.client.post("/posts", json=data, headers=headers)