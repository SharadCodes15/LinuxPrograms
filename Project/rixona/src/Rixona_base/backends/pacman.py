from ..core.executor import Executor,ReturnResult
from ..core.validator import Validator
from .base import PackageBackend

class PacmanBackend(PackageBackend):
    def __init__(self, executor):
        super().__init__(executor)

    def install(self, package_name):
        if not Validator.validatePackageName(package_name):
            raise ValueError("Invalid Pakage Name")
        return self.executor.execute(["sudo","pacman","-S","--needed",package_name])

    def remove(self, package_name):
        if not Validator.validatePackageName(package_name):
            raise ValueError("Invalid Pakage Name")
        return self.executor.execute(["sudo","pacman","-R",package_name])

    def search(self, package_name):
        if not Validator.validatePackageName(package_name):
            raise ValueError("Invalid Pakage Name")
        return self.executor.execute(["pacman","-Ss",package_name])

    def update(self):
        return self.executor.execute(["sudo","pacman","-Syu"])

    def list_installed(self):
        return self.executor.execute(["pacman","-Q"])
