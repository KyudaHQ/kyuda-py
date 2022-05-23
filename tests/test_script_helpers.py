# autopep8: off
# this needs to go before importing script_helpers
import os
os.environ["KYUDA_STEPS"] = '{"foo": true}'

from kyudahq.script_helpers import (steps, export, reload_steps)
# autopep8: on


def test_steps():
    assert steps == {"foo": True}
