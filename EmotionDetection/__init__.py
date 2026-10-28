"""Emotion detection powered by the Skills Network Watson NLP service."""

from . import emotion_detection
from .emotion_detection import emotion_detector

__all__ = ["emotion_detection", "emotion_detector"]
