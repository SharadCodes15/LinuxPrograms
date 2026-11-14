import re
class Validator():
    @staticmethod
    def validate_package_name(self, package_name: str) -> bool:
        if not isinstance(package_name, str):
            return False

        if not package_name or package_name.startswith("-"):
            return False

        # Allow normal Arch package-name characters
        pattern = r"^[A-Za-z0-9@._+-]+$"

        return bool(re.fullmatch(pattern, package_name))