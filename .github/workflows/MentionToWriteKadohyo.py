
message = {
    "content": "Webhookからのテストメッセージだよ"
}


import os

def get_webhook_url(){
  return os.environ.get("WEBHOOK_URL")
}
