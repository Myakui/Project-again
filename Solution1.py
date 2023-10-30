def scenario1():
    from github import Github
    import difflib

    # Замените 'YOUR_TOKEN' на ваш реальный токен
    g = Github('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')

    # Укажите имя пользователя и название репозитория
    user = 'Myakui'
    repo_name = 'Project-again'

    # Получаем репозиторий
    repo = g.get_repo(f'{user}/{repo_name}')

    # Получаем список файлов в репозитории
    files = repo.get_contents("")
    print(files)

    for file in files:
        if file.name.endswith('.txt'):
            file_name = file.name
            previous_content = file.decoded_content.decode('utf-8')

            commits = list(repo.get_commits(path=file_name))

            list_diffs = []
            for commit in reversed(commits):
                current_content = repo.get_contents(file_name, ref=commit.sha).decoded_content.decode('utf-8')

                if current_content != previous_content:
                    # Используем difflib для сравнения текстов
                    d = difflib.Differ()
                    diff = list(d.compare(previous_content.splitlines(), current_content.splitlines()))
                    list_diffs.append(diff)
                    previous_content = current_content
            return list_diffs
print(scenario1())