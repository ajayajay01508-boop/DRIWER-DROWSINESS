"""Dependency-light drowsiness scoring primitives."""
from dataclasses import dataclass
from math import dist


def eye_aspect_ratio(eye):
    if len(eye) != 6:
        raise ValueError("eye must contain exactly 6 landmarks")
    width = dist(eye[0], eye[3])
    if width == 0:
        raise ValueError("eye width must be non-zero")
    return (dist(eye[1], eye[5]) + dist(eye[2], eye[4])) / (2.0 * width)


def mouth_aspect_ratio(mouth):
    if len(mouth) != 20:
        raise ValueError("mouth must contain exactly 20 landmarks")
    width = dist(mouth[12], mouth[16])
    if width == 0:
        raise ValueError("mouth width must be non-zero")
    return (dist(mouth[13], mouth[19]) + dist(mouth[14], mouth[18]) + dist(mouth[15], mouth[17])) / (3.0 * width)


@dataclass
class DrowsinessMonitor:
    ear_threshold: float = 0.22
    mar_threshold: float = 0.60
    consecutive_frames: int = 20
    low_eye_frames: int = 0

    def update(self, ear: float, mar: float) -> dict:
        if not 0 <= ear <= 1.5 or not 0 <= mar <= 3:
            raise ValueError("EAR/MAR outside supported range")
        self.low_eye_frames = self.low_eye_frames + 1 if ear < self.ear_threshold else 0
        alert = self.low_eye_frames >= self.consecutive_frames or mar >= self.mar_threshold
        return {"alert": alert, "ear": ear, "mar": mar, "low_eye_frames": self.low_eye_frames}
