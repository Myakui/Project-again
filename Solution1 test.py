import git
import difflib

def scenario1():
    # Путь к вашему локальному репозиторию
    local_repo_path = 'C:/Users/yakov/Pycharm Projects/Code for GIT'

    # Инициализация репозитория
    repo = git.Repo(local_repo_path)

    # Получаем список файлов в корне репозитория
    files = [item for item in repo.tree().traverse() if item.type == 'blob']

    for file in files:
        if file.name.endswith('.txt'):
            file_name = file.name
            previous_content = file.data_stream.read().decode('utf-8')

            list_diffs = []
            for commit in repo.iter_commits(paths=file_name):
                current_content = commit.tree[file_name].data_stream.read().decode('utf-8')

                if current_content != previous_content:
                    # Используем difflib для сравнения текстов
                    d = difflib.Differ()
                    diff = list(d.compare(previous_content.splitlines(), current_content.splitlines()))
                    list_diffs.append(diff)
                    previous_content = current_content
            return list_diffs

# Вызов функции
print(scenario1())
