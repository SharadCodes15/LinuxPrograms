''' assume pkg managers ie pacmand apt yay flatpak similar operation but diff commands '''

'''
                    Architecture (Abstract base class)
                install
                remove
                search
                update
                list_Installed

                pacman Backend      Apt Backend
                yay Backend         Flatpak Backend

                examples : packman.install("firefox")
                           apt.install("firefox")

            polymorphism -> same method name . diffrent implementation
'''

'''
            Requirements
                ABC
                @abstractmethod
                Inheritance
                super()
'''

from abc import ABC, abstractmethod
from ..core.executor import Executor, ReturnResult
class PackageBackend(ABC):

    def __init__(self,executor:Executor):
        self.executor = executor

    @abstractmethod
    def install(self, package_name:str)->ReturnResult:
        pass

    @abstractmethod
    def remove(self, package_name:str)->ReturnResult:
        pass

    @abstractmethod
    def search(self, package_name:str)->ReturnResult:
        pass

    @abstractmethod
    def update(self)->ReturnResult:
        pass

    @abstractmethod
    def list_installed(self)->ReturnResult:
        pass

