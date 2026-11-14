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
