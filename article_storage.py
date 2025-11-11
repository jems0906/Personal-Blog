import os
import json
from datetime import datetime

ARTICLES_DIR = os.path.join(os.path.dirname(__file__), 'articles')

# Each article is stored as a JSON file: {"title": ..., "content": ..., "date": ...}
def list_articles():
    articles = []
    for fname in os.listdir(ARTICLES_DIR):
        if fname.endswith('.json'):
            with open(os.path.join(ARTICLES_DIR, fname), 'r', encoding='utf-8') as f:
                data = json.load(f)
                data['id'] = fname[:-5]
                articles.append(data)
    articles.sort(key=lambda x: x['date'], reverse=True)
    return articles

def get_article(article_id):
    path = os.path.join(ARTICLES_DIR, f'{article_id}.json')
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_article(article_id, title, content, date=None):
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')
    data = {'title': title, 'content': content, 'date': date}
    with open(os.path.join(ARTICLES_DIR, f'{article_id}.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f)

def delete_article(article_id):
    path = os.path.join(ARTICLES_DIR, f'{article_id}.json')
    if os.path.exists(path):
        os.remove(path)
