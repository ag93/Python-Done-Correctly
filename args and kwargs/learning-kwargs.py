# -*- coding: utf-8 -*-

def blog_posts_3(**kwargs):
    for title, post in kwargs.items():
        print(title,post)

blog_posts_3(blog_1 = 'I am so awesome',
             blog_2 = 'Cars are cool.',
             blog_3 = 'Aww look at my cat.')