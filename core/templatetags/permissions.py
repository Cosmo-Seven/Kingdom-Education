from django import template

register = template.Library()


@register.filter
def has_role_permission(user, permission_codename):
    if user.is_authenticated and hasattr(user, "has_permission"):
        return user.has_permission(permission_codename)
    return False


@register.filter
def can(user, permission):
    """
    Single permission check
    """
    if not user.is_authenticated:
        return False

    if permission == "is_staff":
        return user.is_staff

    if permission == "is_superuser":
        return user.is_superuser

    if permission == "not_superuser":
        return not user.is_superuser

    return hasattr(user, "has_permission") and user.has_permission(permission)


@register.filter
def can_any(user, permissions):
    """
    permissions = list OR comma-separated string
    """
    if not permissions:
        return False

    if isinstance(permissions, str):
        permissions = [p.strip() for p in permissions.split(",")]

    return any(can(user, perm) for perm in permissions)
