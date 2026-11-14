from ..core.detector import Detector
class PackageRouter:
    def __init__(self,detector:Detector,backends:dict):
        self.detector = detector
        self.backends = backends

    def get_available_backends(self):
        return self.detector.detect_pkg_manager()

    def get_backend(self, name: str):
        if name not in self.backends:
            raise ValueError(f"Backend '{name}' is not available")

        return self.backends[name]