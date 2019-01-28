"""RLBotTraining
Runs the training exercise playlist in the given python file.
The playlist has to be provided via a make_default_playlist() function.

Usage:
  rlbottraining run_module <python_file> [--history_dir=<path>]
  rlbottraining (-h | --help)
  rlbottraining --version

Options:
  -H --history_dir=<path>  Where to persist results of the exercises.
  -h --help                Show this screen.
  --version                Show version.
"""

from pathlib import Path

from docopt import docopt

from rlbottraining.version import __version__
from rlbottraining.exercise_runner import run_module

if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)
    print(arguments)
    if arguments['run_module']:
        run_module(
            Path(arguments['<python_file>']),
            history_dir=arguments['--history_dir']
        )
