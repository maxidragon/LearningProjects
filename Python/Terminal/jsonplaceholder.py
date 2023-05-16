import requests
from pprint import pprint

def get_content(url):
    r = requests.get(url)
    content = r.json()
    return content

users = 'https://jsonplaceholder.typicode.com/users'
posts = 'https://jsonplaceholder.typicode.com/posts'
todos = 'https://jsonplaceholder.typicode.com/todos'
users_content = get_content(users)
posts_content = get_content(posts)
todos_content = get_content(todos)
#pprint(posts_content)



#users = {}
# for i in users_content:
#     users[i['id']] = i['username']
# print(users)

#ile postow napisal user (slownik z userid i liczba postow)
# users_posts = {}
# for i in users_content:
#     users_posts[i['id']] = 0
# print(users_posts)
# for i in posts_content:
#     users_posts[i['userId']] += 1
# print(users_posts)
users_todos = {}
for user in users_content:
    users_todos[user['id']] = 0
print(users_todos)
for todo in todos_content:
    if todo['completed']:
        users_todos[todo['userId']] += 1
print(users_todos)
users_with_completed_tasks = []
for user_id in users_todos:
    if users_todos[user_id] == max(users_todos.values()):
        users_with_completed_tasks.append(user_id)
print(users_with_completed_tasks)
for user in users_content:
    if user['id'] in users_with_completed_tasks:
        print(user['name'])
        print(user['address'])
