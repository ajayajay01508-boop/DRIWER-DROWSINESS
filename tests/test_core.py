import unittest
from drowsiness.core import DrowsinessMonitor, eye_aspect_ratio


class CoreTests(unittest.TestCase):
    def test_ear(self):
        eye = [(0, 0), (1, 1), (3, 1), (4, 0), (3, -1), (1, -1)]
        self.assertAlmostEqual(eye_aspect_ratio(eye), 0.5)

    def test_temporal_alarm_and_reset(self):
        monitor = DrowsinessMonitor(consecutive_frames=3)
        self.assertFalse(monitor.update(.1, .2)["alert"])
        self.assertFalse(monitor.update(.1, .2)["alert"])
        self.assertTrue(monitor.update(.1, .2)["alert"])
        self.assertFalse(monitor.update(.3, .2)["alert"])

    def test_yawn_alarm(self):
        self.assertTrue(DrowsinessMonitor().update(.3, .8)["alert"])

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            DrowsinessMonitor().update(-1, .2)


if __name__ == "__main__":
    unittest.main()
