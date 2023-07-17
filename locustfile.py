from locust import HttpUser, task, between


class ArticleTest(HttpUser):
    wait_time = between(1, 2)

    # def on_start(self):
    #     self.client.post("/login", json={"username": "foo", "password": "bar"})

    @task
    def list_(self):
        self.client.get("article")
