# -*- coding: utf-8 -*-

blog_1 = 'Nartuo is awesome'
blog_2 = 'Muse is awesome'
blog_3 = 'Dogs are awesome'


def blog_posts_2(regular_arg, *args):
    print(regular_arg)
    for post in args:
        print(post)

blog_posts_2('Blog of Awesomeness! :',blog_1,blog_2,blog_3)
