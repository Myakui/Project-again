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

for file in files:
    if file.name.endswith('.txt'):
        file_name = file.name
        previous_content = file.decoded_content.decode('utf-8')

        commits = list(repo.get_commits(path=file_name))

        for commit in reversed(commits):
            current_content = repo.get_contents(file_name, ref=commit.sha).decoded_content.decode('utf-8')

            if current_content != previous_content:
                print(f"Commit Message: {commit.commit.message}")

                # Используем difflib для сравнения текстов
                d = difflib.Differ()
                diff = list(d.compare(previous_content.splitlines(), current_content.splitlines()))

                # Отображаем изменения
                for line in diff:
                    if line.startswith('  '):
                        print("  " + line[2:])  # Неизмененная строка
                    elif line.startswith('- '):
                        print("- " + line[2:])  # Удаленная строка
                    elif line.startswith('+ '):
                        print("+ " + line[2:])  # Добавленная строка
                print('')

                previous_content = current_content

