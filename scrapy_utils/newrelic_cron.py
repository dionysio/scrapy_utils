from traceback import format_exc
from functools import wraps

try:
    import newrelic.agent
    newrelic.agent.initialize()
except ImportError:
    pass


def newrelic_cron(f):
    @wraps(f)
    def _wrapped(*args, **kwargs):
        result = None
        completed = True
        try:
            result = f(*args, **kwargs)
        except:
            completed = False
            result = format_exc()
        finally:
            event_name = f'{f.__name__}_event'
            result = {
                "eventType": event_name,
                "result": result,
                "completed": completed
            }
            newrelic.agent.record_custom_event(event_name, result, newrelic.agent.application())

    return _wrapped
