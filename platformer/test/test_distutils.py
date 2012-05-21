
from platformer.test.test_platform import TestPlatform as BasicTest
from platformer.distutils_platform import DistutilsPlatform
import py

class TestDistutils(BasicTest):
    platform = DistutilsPlatform()

    def test_nice_errors(self):
        py.test.skip("Unsupported")
