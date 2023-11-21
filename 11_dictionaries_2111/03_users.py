import requests as r

url = 'https://jsonplaceholder.typicode.com/posts'
url2 = 'https://jsonplaceholder.typicode.com/comments'
posts_list = r.get(url).json()  # обратиться по ссылке и получить json
comments_list = r.get(url2).json()

# посчитать количество комментариев к посту с id 5
com_count = 0
for comment in comments_list:
    if comment['postId'] == 5:
        com_count += 1
print(f'К посту №5 оставили комментариев: {com_count}')

social_media = {}  # здесь мы будем хранить все посты и комментарии к ним
for post in posts_list:
    social_media[post['id']] = {"title": post["title"],
                                "body": post["body"],
                                "comments": []}  # сохраняю пост и комментрии как отдельный словарь
for comment in comments_list:  # перебираю комментарии
    post = social_media[comment['postId']]["comments"]  # сохраняю пост в переменной для добавления комментариев
    comm = {"id": comment["id"],
            "title": comment["name"],
            "body": comment["body"]}  # достаю всю информацию из комментария (нужную)
    post.append(comm)  # добавляю комментарий в список с комментариями

for post in social_media:
    print(f'Post id: {post}\nPost title: {social_media[post]["title"]}')
    print(f'Post body: {social_media[post]["body"]}')
    print('\nComments:')
    for comment in social_media[post]["comments"]:
        print(f"\t\tHeading: {comment['title']}\n\t\t Text: {comment['body']}")
