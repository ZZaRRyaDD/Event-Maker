from rest_framework import permissions

from apps.events.models import Event


class EventMember(permissions.BasePermission):
    """Custom permission class for members of event."""

    def has_permission(self, request, view) -> bool:
        return view.action != "finish"

    def has_object_permission(self, request, view, obj) -> bool:
        if request.method in ("PUT", "PATCH", "DELETE"):
            return False
        return request.user in obj.members.all() if obj.is_private else True


class EventOwner(permissions.BasePermission):
    """Custom permission class for owner of event."""

    def has_permission(self, request, view) -> bool:
        return (
            Event.objects.filter(
                id=request.parser_context["kwargs"]["pk"],
            ).first().owner_id ==
            request.user.id
        )

    def has_object_permission(self, request, view, obj) -> bool:
        return request.user == obj.owner
