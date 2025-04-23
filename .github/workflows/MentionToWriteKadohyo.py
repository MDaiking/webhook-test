webhook_url = os.environ.get("WEBHOOK_URL")

message = {
    "content": "Webhookからのテストメッセージだよ"
}


headers = {
    'Content-Type': 'application/json'
}


response = requests.post(webhook_url, data=json.dumps(message), headers=headers)

if response.status_code != 204:
    print(f"エラーが発生しました: {response.status_code}")
