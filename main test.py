import requests

# Указываем имя пользователя, название репозитория и токен
user = 'Myakui'
repo = 'Project-again'
token = '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'

# Отправляем GET-запрос к API GitHub для получения списка коммитов
response = requests.get(f'https://api.github.com/repos/{user}/{repo}/commits',
                        headers={'Authorization': f'token {token}'})

# Если запрос успешен, извлекаем данные из ответа в формате JSON
if response.status_code == 200:
    commits = list(response.json())

    # Инициализируем переменную для хранения предыдущего коммита
    previous_commit = None

    # Перебираем список коммитов
    for commit in reversed(commits):
        commit_sha = commit['sha']

        # Если это не первый коммит, сравниваем его с предыдущим
        if previous_commit:
            diff_url = f'https://api.github.com/repos/{user}/{repo}/compare/{previous_commit}...{commit_sha}'
            diff_response = requests.get(diff_url, headers={'Authorization': f'token {token}'})

            # Если запрос успешен, извлекаем данные из ответа в формате JSON
            if diff_response.status_code == 200:
                diff = diff_response.json()

                # Перебираем изменения в коммите
                for file in diff['files']:
                    if file['filename'].endswith('.txt'):
                        # Выводим информацию о файле и количестве изменений
                        print(f'File: {file["filename"]}')
                        print(f'Changes: {file["changes"]} changes')

                        # Перебираем добавленные строки
                        for line in file["patch"].split('\n'):
                            if line.startswith('+'):
                                print(f'Added: {line[1:]}')
                        print()

            else:
                # Если запрос не успешен, выводим сообщение об ошибке
                print(f'Error: {diff_response.status_code} - {diff_response.text}')

        # Обновляем предыдущий коммит
        previous_commit = commit_sha

# Если запрос не успешен, выводим сообщение об ошибке
else:
    print(f'Error: {response.status_code} - {response.text}')
