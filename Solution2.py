import git
import difflib


def get_commit_changes(repo, file_name):
    commits = list(repo.iter_commits(paths=file_name))

    list_diffs = []
    previous_content = None

    for commit in reversed(commits):
        current_content = commit.tree[file_name].data_stream.read().decode('utf-8')

        if previous_content:
            d = difflib.Differ()
            diff = list(d.compare(previous_content.splitlines(), current_content.splitlines()))

            diff_result = []

            for line in diff:
                if line.startswith(' '):
                    continue
                elif line.startswith('- '):
                    diff_result.append('-' + line[2:])
                elif line.startswith('+ '):
                    diff_result.append('+' + line[2:])

            if diff_result:
                list_diffs.append(diff_result)

        previous_content = current_content

    return list_diffs


def scenario(local_repo_path):
    # Инициализация репозитория
    repo = git.Repo(local_repo_path)

    for item in repo.tree().traverse():
        if item.type == 'blob' and item.name.endswith('.txt'):
            file_name = item.name
            list_diffs = get_commit_changes(repo, file_name)
            print(list_diffs)
            if list_diffs:
                print(f'File: {file_name}')
                for diff in list_diffs:
                    for line in diff:
                        print(line)
    return list_diffs

# Укажите путь к вашему локальному репозиторию
def scenario1():
    local_repo_path = 'C:/Users/yakov/Pycharm Projects/Code for GIT'
    return scenario(local_repo_path)

