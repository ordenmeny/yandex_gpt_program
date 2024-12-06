import requests

URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
IAM_TOKEN = "t1.9euelZrNm4zGicqZiszJl8fGipWXj-3rnpWakZiLlouOyJ2OlJeLmJqex5Hl8_dYNTRF-e9QOWBj_N3z9xhkMUX571A5YGP8zef1656Vmsmam42WyJ2OnZeUmp2TyZaa7_zF656Vmsmam42WyJ2OnZeUmp2TyZaa.EpCqJ3VwxqFxw9P0IEEzRUXhgLSXvlEIRlX58XusJtorAxiTrYjoby_jMjmskNAkO-WcesIhGzesVaEmb5aQBw"
FOLDER_ID = "b1g88edpbhf5q2b4a37c"


def run(iam_token, folder_id, user_text):
    # Собираем запрос
    data = {}
    # Указываем тип модели
    data["modelUri"] = f"gpt://{folder_id}/yandexgpt/latest"
    # Настраиваем опции
    data["completionOptions"] = {"temperature": 0.3, "maxTokens": 1000}
    # Указываем контекст для модели
    data["messages"] = [
        {
            "role": "system",
            "text": "Нужно придумать кринжовую шутку. На вход поступает тема шутки."
        },

        {
            "role": "user",
            "text": f"{user_text}"
        },
    ]

    # Отправляем запрос
    response = requests.post(
        URL,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {iam_token}"
        },
        json=data,
    ).json()

    # Распечатываем результат
    return response


text = "Шутка про айтишников"
run_res = run(IAM_TOKEN, FOLDER_ID, text)
gpt_response_text = run_res["result"]["alternatives"][0]["message"]["text"]
print(gpt_response_text)
