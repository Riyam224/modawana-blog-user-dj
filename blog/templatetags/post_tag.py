from django import template
from modawana.models import Post, Comment

register = template.Library()
@register.inclusion_tag('latest_posts.html')
def latest_posts():
    context = {
        'l_posts': Post.objects.all()[0:5],
    }
    return context


@register.inclusion_tag('latest_comments.html')
def latest_comments():
    context = {
        'l_comments': Comment.objects.filter(active=True)[:5],
    }
    return context
