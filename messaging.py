from functools import wraps
from collections import defaultdict


class EventBase:
    ...


class InMemoryEventDispatcher:
    def __init__(self):
        self._handlers = defaultdict(set)

    def add_event_handler(self, event_class: type[EventBase], event_handler: callable):
        self._handlers[event_class].add(event_handler)

    def dispatch(self, event: type[EventBase]):
        event_class = type(event)
        for event_handler in self._handlers[event_class]:
            event_handler(event)


dispatcher = InMemoryEventDispatcher()


def command(fn):
    """"decorator"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Executing command {fn.__module__}.{fn.__name__}", args[1:], kwargs)
        event = fn(*args, **kwargs)
        if isinstance(event, EventBase):
            print("Publishing event", event)
            dispatcher.dispatch(event)
        return event
    return wrapper