from logfire import span
import asyncio
from functools import wraps

def span_decorator(span_name, attrs=None, capture_return_value=True):
    def decorator(func):
        def build_dynamic_name(args, kwargs):
            dynamic_name = span_name
            if attrs:
                arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
                arg_map = dict(zip(arg_names, args))
                arg_map.update(kwargs)
                attr_str = ",".join(f"{a}={arg_map.get(a)}" for a in attrs if a in arg_map)
                if attr_str:
                    dynamic_name = f"{span_name}[{attr_str}]"
            return dynamic_name
        if asyncio.iscoroutinefunction(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                with span(build_dynamic_name(args, kwargs)) as s:
                    result = await func(*args, **kwargs)
                    if capture_return_value:
                        s.set_attribute("return_value", result)
                    return result
            return async_wrapper
        else:
            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                with span(build_dynamic_name(args, kwargs)) as s:
                    result = func(*args, **kwargs)
                    if capture_return_value:
                        s.set_attribute("return_value", result)
                    return result
            return sync_wrapper
    return decorator
