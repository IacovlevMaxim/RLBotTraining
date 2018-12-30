"""
This module exists to provide common types of gading for exercises
als allow composition of them.
"""
from .event_detector import PlayerEventDetector, PlayerEvent, PlayerEventType
from .grader import Grader, GraderExercise, TrainingTickPacket
from .compound_grader import CompoundGrader
from .timeout import FailOnTimeout, PassOnTimeout
from .goal_grader import StrikerGrader, GoalieGrader
