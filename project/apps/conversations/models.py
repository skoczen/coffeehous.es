from django.db import models as django_models
from neo4django.db import models
from main_site.models import BaseModel


class ArticleUpload(BaseModel):
    article = django_models.FileField(upload_to="article_uploads")


class Person(models.NodeModel):
    name = models.StringProperty()
    email = models.EmailProperty()

    friends = models.Relationship(
        'self',
        rel_type='friends_with'
    )


class Idea(models.NodeModel):
    poster = models.Relationship(
        Person,
        rel_type='brought',
        related_name='ideas'
    )

    title = models.StringProperty()
    summary = models.StringProperty()
    url = models.StringProperty()
    article_upload_pk = models.IntegerProperty()


class CommentBody(object):
    posted_at = models.DateTimeProperty(auto_now_add=True)
    edited_at = models.DateTimeProperty()
    body = models.StringProperty()


class ConversationSpark(models.NodeModel, CommentBody):
    idea = models.Relationship(
        Idea,
        rel_type='inspired',
        related_name='sparks'
    )
    poster = models.Relationship(
        Person,
        rel_type='wrote',
        related_name='sparks'
    )


class Conversation(models.NodeModel):
    spark = models.Relationship(
        Idea,
        rel_type='inspired',
        related_name='conversations'
    )


class Comment(models.NodeModel, CommentBody):
    conversation = models.Relationship(
        Conversation,
        rel_type='inspired',
        preserve_ordering=True,
        related_name='comments',
    )
    author = models.Relationship(
        Person,
        rel_type='wrote',
        related_name='comments'
    )


# def create_user_profile(sender, instance, created, **kwargs):
#     if created and not Person.objects.filter(user=instance).count() > 0:
#         Person.objects.create(user=instance)

# post_save.connect(create_user_profile, sender=User, dispatch_uid="create_user_profile")
