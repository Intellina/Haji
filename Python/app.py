from fastapi import FastAPI

app = FastAPI(title="Grafana Grafana", version="1.0.0")

users = {"1":"Budi", "2":"Sasuke", "3":"Haruno"}

@app.get("/")
async def MainRoute():
  """
  Main Router
  """
  return {"result":"Grafana Metrics !"}

@app.get("/GetUser/{user}")
async def GetUserC(user : str):
  """
  Get User
  """
  if user in users:
    # User Available
    result = users[user]
  else:
    # User Unavailable !
    result = "User Unavailable !"
  return {"result":result}
