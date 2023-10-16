import requests

# Указываем имя пользователя и название репозитория
user = 'Myakui'
repo = 'Project-again'

# Определяем переменную для хранения предыдущего содержимого файла
previous_file_content = None

# Отправляем GET-запрос к API GitHub для получения списка коммитов
response = requests.get(f'https://api.github.com/repos/{user}/{repo}/commits', headers={'Authorization': 'token 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'})

# Если запрос успешен, извлекаем данные из ответа в формате JSON
if response.status_code == 200:
    commits = response.json()

    # Изменяем порядок коммитов на обратный
    commits = reversed(commits)

    # Перебираем список коммитов
    for commit in commits:
        commit_id = commit['sha']
        commit_date = commit['commit']['author']['date']
        commit_author = commit['commit']['author']['name']
        commit_message = commit['commit']['message']

        # Отправляем GET-запрос к API GitHub для получения изменений в коммите
        diff_response = requests.get(f'https://api.github.com/repos/{user}/{repo}/commits/{commit_id}')

        # Если запрос успешен, извлекаем данные из ответа в формате JSON
        if diff_response.status_code == 200:
            diff = diff_response.json()

            # Перебираем изменения в коммите
            for file in diff['files']:
                if file['filename'].endswith('.txt'):
                    # Выводим информацию о файле и количестве изменений
                    print(f'File: {file["filename"]}')
                    print(f'Changes: {file["changes"]} changes')

                    # Если это первый коммит, читаем его содержимое/Проверка на пустой файл
                    if previous_file_content is None:
                        previous_file_content = requests.get(file['raw_url']).text
                        print('Empty file')
                        print()
                    else:
                        # Если это не первый коммит, сравниваем содержимое файла с предыдущим коммитом
                        current_file_content = requests.get(file['raw_url']).text
                        if current_file_content != previous_file_content:
                            print('File Content Change:')
                            print(current_file_content)
                            print()

                        # Обновляем предыдущее содержимое файла
                        previous_file_content = current_file_content

        else:
            # Если запрос не успешен, выводим сообщение об ошибке
            print(f'Error: {diff_response.status_code} - {diff_response.text}')

    # Если запрос не успешен, выводим сообщение об ошибке
else:
    print(f'Error: {response.status_code} - {response.text}')
