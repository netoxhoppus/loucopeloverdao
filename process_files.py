import os

def process_file(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo {filepath}: {e}")
        return

    lines = content.splitlines()
    new_content = ""
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line:  # Ignora linhas em branco
            new_content += cleaned_line + "\n"

    try:
        with open(filepath, 'w') as f:
            f.write(new_content)
    except Exception as e:
        print(f"Erro ao escrever no arquivo {filepath}: {e}")


files = [
    'blog/__init__.py', 'blog/admin.py', 'blog/apps.py', 'blog/context_processors.py',
    'blog/models.py', 'blog/tests.py', 'blog/urls.py', 'blog/views.py',
    'core/__init__.py', 'core/asgi.py', 'core/settings.py', 'core/urls.py', 'core/wsgi.py',
    'blog/templates/blog/assets.css.html', 'blog/templates/blog/assets.js.html',
    'blog/templates/blog/base.html', 'blog/templates/blog/footer.html',
    'blog/templates/blog/header.html', 'blog/templates/blog/home.html',
    'blog/templates/blog/post.html', 'blog/templates/blog/trending_area.html',
    'blog/templates/blog/trending_now.html'
]

for file in files:
    if file.endswith(('.py', '.html')):
        process_file(file)
