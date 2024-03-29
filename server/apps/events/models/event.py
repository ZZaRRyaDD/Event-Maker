
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Event(BaseModel):
    """Model of Event."""

    name = models.CharField(
        max_length=128,
        verbose_name=_("Name of event"),
    )
    description = models.TextField(
        verbose_name=_("Description of event"),
    )
    address = models.TextField(
        verbose_name=_("Address/link of event"),
    )
    datetime_spending = models.DateTimeField(
        verbose_name=_("Event's time spending"),
    )
    is_online = models.BooleanField(
        default=False,
        verbose_name=_("Is online event"),
    )
    is_private = models.BooleanField(
        default=False,
        verbose_name=_("Is private event"),
    )
    is_finished = models.BooleanField(
        default=False,
        verbose_name=_("Is finished event"),
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="events_owner",
        verbose_name=_("Owner of event"),
    )
    members = models.ManyToManyField(
        User,
        related_name="events_member",
        verbose_name=_("Members of event"),
    )

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self) -> str:
        return f"Event {self.name}"
