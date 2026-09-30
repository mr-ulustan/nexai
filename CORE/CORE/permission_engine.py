import json


class PermissionEngine:
    def __init__(self, permissions_file="permissions.json"):
        with open(permissions_file, "r", encoding="utf-8") as file:
            self.permissions = json.load(file)

    def can_ai(self, permission):
        ai_permissions = self.permissions["ai"]["permissions"]

        if permission in self.permissions["protected_permissions"]:
            return False

        return permission in ai_permissions


if __name__ == "__main__":
    engine = PermissionEngine()

    tests = [
        "read_information",
        "analyze_information",
        "manage_permissions",
        "modify_core",
        "disable_safety",
        "self_modify"
    ]

    for permission in tests:
        result = engine.can_ai(permission)
        print(f"{permission}: {'ALLOWED' if result else 'DENIED'}")
