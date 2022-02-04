import uuid
from django.db import models
from taggit.managers import TaggableManager

from django.utils.translation import gettext_lazy as _
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


# Create your models here.
class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Todo(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, max_length=50, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    due_date = models.DateField(blank=True, null=True)
    tags = TaggableManager(through=UUIDTaggedItem)
    status = models.CharField(
        default="OPEN", max_length=10, blank=False, null=False)
