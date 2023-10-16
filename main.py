import base64
import requests

# Указываем имя пользователя и название репозитория
user = 'Myakui'
repo = 'Project-again'

# Отправляем GET-запрос к API GitHub для получения списка файлов в репозитории
response = requests.get(f'https://api.github.com/repos/{user}/{repo}/contents',
                        headers={'Authorization': 'token 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'})

# Если запрос успешен, извлекаем данные из ответа в формате JSON
if response.status_code == 200:
    files = response.json()

    # Перебираем список файлов
    for file in files:
        if file['type'] == 'file' and file['name'].endswith('.txt'):
            # Получаем имя файла и его путь
            file_name = file['name']
            file_path = file['path']

            # Выводим информацию о файле
            print(f'File Name: {file_name}')
            print(f'File Path: {file_path}')

            # Отправляем GET-запрос к API GitHub для получения коммитов для данного файла
            commits_response = requests.get(f'https://api.github.com/repos/{user}/{repo}/commits?path={file_path}',
                                            headers={'Authorization': 'token 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'})

            # Если запрос успешен, извлекаем данные из ответа в формате JSON
            if commits_response.status_code == 200:
                commits = commits_response.json()

                # Перебираем список коммитов и выводим информацию о каждом коммите
                for i, commit in enumerate(commits):
                    commit_id = commit['sha']
                    commit_date = commit['commit']['author']['date']
                    commit_author = commit['commit']['author']['name']
                    commit_message = commit['commit']['message']

                    # Выводим информацию о коммите
                    print(f'Commit Number: {i + 1}')
                    print(f'Commit ID: {commit_id}')
                    print(f'Commit Date: {commit_date}')
                    print(f'Commit Author: {commit_author}')
                    print(f'Commit Message: {commit_message}')

                    # Отправляем GET-запрос к API GitHub для получения содержимого файла из коммита
                    file_content_response = requests.get(f'https://api.github.com/repos/{user}/{repo}/contents/{file_path}?ref={commit_id}',
                                                        headers={'Authorization': 'token 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'})

                    # Если запрос успешен, извлекаем данные из ответа в формате JSON
                    if file_content_response.status_code == 200:
                        file_content = file_content_response.json()

                        # Декодируем содержимое файла из base64
                        content = file_content['content']
                        content = content.encode('utf-8')
                        content = base64.b64decode(content)
                        content = content.decode('utf-8')

                        # Выводим содержимое файла
                        print('File Content:')
                        print(content)
                        print('---------------------------------\n')

                    else:
                        # Если запрос не успешен, выводим сообщение об ошибке
                        print(f'Error: {file_content_response.status_code} - {file_content_response.text}')

                # Проверка на пустой список коммитов
                if not commits:
                    print("No commits found for this file.")

            else:
                # Если запрос не успешен, выводим сообщение об ошибке
                print(f'Error: {commits_response.status_code} - {commits_response.text}')

    # Проверка на пустой список файлов
    if not files:
        print("No .txt files found in the repository.")

else:
    # Если запрос не успешен, выводим сообщение об ошибке
    print(f'Error: {response.status_code} - {response.text}')
