import splunk_integration

if __name__ == "__main__":
    splunk = splunk_integration.SplunkIntegration(
        host="localhost",
        port=8089,
        username="admin",
        password="testpwd!"
    )
    
    try:
        splunk.connect()
        print("Connected to Splunk")
        results = splunk.run_query("search index=_internal | head 10")
        for result in results:
            print(result)
    finally:
        splunk.close()