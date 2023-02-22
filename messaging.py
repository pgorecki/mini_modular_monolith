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
        for fn in self._handlers[event_class]:
            fn(event)


dispatcher = InMemoryEventDispatcher()


def command_handler(fn):
    """"command handler decorator"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Executing command {fn.__module__}.{fn.__name__}", args[1:], kwargs)
        event = fn(*args, **kwargs)
        if isinstance(event, EventBase):
            print("Publishing event", event)
            dispatcher.dispatch(event)
        return event
    return wrapper


def event_handler(event_class):
    """"event handler decorator"""

    assert issubclass(event_class, EventBase)

    def _event_handler(fn):
        """"event handler decorator"""
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"Handling event {args[1]} via {fn}")
            fn(*args, **kwargs)

        wrapper._handled_event = event_class
        return wrapper

    return _event_handler


def register_event_handlers(module_instance):
    for name in dir(module_instance):
        fn = getattr(module_instance, name)
        if callable(fn) and hasattr(fn, '_handled_event'):
            event_type = getattr(fn, '_handled_event')
            print(f"Registering event {event_type.__name__} handler as {fn}")
            dispatcher.add_event_handler(event_type, fn)