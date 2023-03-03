from locust import HttpUser, between, task

class MyUser(HttpUser):
    # Setting a wait time of between two numbers
    wait_time=  between(5,15)

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_users(self):
        self.client.get("/users")

    # Defining a task to create new post on the API
    @task
    def create_post(self):
        # Defininf the data to be posted
        data = {
            "title": "NEW POST",
            "body": "This is a new post",
            "userId": 1
        }
        headers = {"Content-Type": "application/json"}
        self.client.post("/posts", json= data, headers=headers)