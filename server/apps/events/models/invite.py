from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Invite(BaseModel):
    """Model of Invite."""

    event = models.ForeignKey(
        "events.Event",
        on_delete=models.CASCADE,
        verbose_name=_("Event of invite"),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="invites",
        verbose_name=_("User of invite"),
    )
    is_accepted = models.BooleanField(
        default=False,
        verbose_name=_("Accept user invite or not"),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active invite or not"),
    )

    class Meta:
        verbose_name = "Invite"
        verbose_name_plural = "Invites"

    def __str__(self) -> str:
        return f"Invite {self.event} and {self.user}"
