import requests

# Указываем имя пользователя, название репозитория и токен
user = 'Myakui'
repo_name = 'Project-again'
token = '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'

# Отправляем GET-запрос к API GitHub для получения списка коммитов
response = requests.get(f'https://api.github.com/repos/{user}/{repo_name}/commits', headers={'Authorization': f'token {token}'})

# Если запрос успешен, извлекаем данные из ответа в формате JSON
if response.status_code == 200:
    commits = list(reversed(response.json()))  # Обратный порядок коммитов

    # Перебираем список коммитов
    for commit in commits:
        commit_sha = commit['sha']

        # Отправляем GET-запрос к API GitHub для получения дерева файлов в коммите
        tree_response = requests.get(f'https://api.github.com/repos/{user}/{repo_name}/commits/{commit_sha}',
                                    headers={'Authorization': f'token {token}'})

        # Если запрос успешен, извлекаем данные из ответа в формате JSON
        if tree_response.status_code == 200:
            tree = tree_response.json()
            # Выводим разделитель для каждого коммита
            print('----------------------')

            # Перебираем файлы в коммите
            for file in tree['files']:
                if file['filename'].endswith('.txt'):
                    # Выводим имя файла
                    print(f'File: {file["filename"]}')

                    # Отправляем GET-запрос к API GitHub для получения содержимого файла
                    file_content_response = requests.get(file['raw_url'])

                    # Если запрос успешен, извлекаем текст из файла
                    if file_content_response.status_code == 200:
                        file_content = file_content_response.text

                        # Выводим изменения в файле с символами + и -
                        lines = file_content.split('\n')
                        for line in lines:
                            print(line)

        else:
            # Если запрос не успешен, выводим сообщение об ошибке
            print(f'Error: {tree_response.status_code} - {tree_response.text}')

else:
    # Если запрос не успешен, выводим сообщение об ошибке
    print(f'Error: {response.status_code} - {response.text}')
