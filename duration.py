from datetime import datetime


def log_time(func):
    def wrap_function(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        hours = duration.seconds // 3600
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60
        print(f"total_time:{hours}:{minutes}:{seconds}")
        return result

    return wrap_function
