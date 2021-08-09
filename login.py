import http.client

conn = http.client.HTTPSConnection("dev-kotbr190.us.auth0.com")

payload = "{\"client_id\":\"DrCvCEzLGmpRbuzvBhmWQNQMBeB2RfRY\",\"client_secret\":\"m1Nb6RAhZ7zEKNuEa3yI3Eth7ATjDoiG1Vwk2YpB-PXWiJXzusauFMVfP11CIL6Z\",\"audience\":\"cap\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))