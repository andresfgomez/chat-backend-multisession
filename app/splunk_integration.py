import splunklib.client as splunk_client

class SplunkIntegration:
    host: str
    port: int
    username: str
    password: str
    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        self.service = splunk_client.connect(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            scheme="https"
        )

    def run_query(self, query: str):
        job = self.service.jobs.create(query)
        while not job.is_done():
            pass
        return list(job.results())

    def close(self):
        self.service.logout()