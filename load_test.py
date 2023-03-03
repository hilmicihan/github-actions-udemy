from locust import HttpUser, between, task
# Setting a wait time of between 5 and 15 seconds for each user action
class MyUser(HttpUser):
    wait_time = between(5, 15)

    # Defining a task to get all posts from the API
    @task
    def get_posts(self):
        self.client.get("/posts")

    # Defining a task to get all users from the API
    @task
    def get_users(self):
        self.client.get("/users")

    # Defining a task to create a new post on the API
    @task
    def create_post(self):
        # Defining the data to be posted
        data = {
            "title": "New Post",
            "body": "This is a new post",
            "userId": 1
        }
        # Defining the headers to be sent with the post request
        headers = {"Content-Type": "application/json"}
        # Sending a post request to create a new post with the specified data and headers
        self.client.post("/posts", json=data, headers=headers)
