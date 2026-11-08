import shutil

class Detector:
    def __init__(self):
        self.managers  = [
                    "apt",
                    "pacman",
                    "yay",
                    "flatpak",
                    "paru"
                ]
        self.available = []
        self.disto = "unknown"

    def detect_pkg_manager(self):
        for manager in self.managers:
            if shutil.which(manager):
                self.available.append(manager)
        return self.available

    def detect_distro(self):
        try:
            with open("/etc/os-release") as file:
                for line in file:
                    if line.startswith("ID="):
                        return line.strip().split("=",1)[1].strip('"')
        except FileNotFoundError:
            return "Distro Detection Failed"

        return "unknown"

if __name__ == '__main__':
    detector = Detector()
    manager = detector.detect_pkg_manager()
    distro = detector.detect_distro()

    print("-"*35)
    print(f"| {'DISTRO' :<10} | {distro:<18} |")
    print("-"*35)
    print(f"| {'MANAGER(s)' :<10} | {', '.join(manager):<18} |")
    print("-"*35)




    