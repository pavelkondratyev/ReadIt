def check_contents(post):
    return False


def check_time(post, time_after):
    if time_after < post.created_utc:
        return True


def check_title(post):
    return False


def check_source(post):
    return False


def check_post(post, time_after):
    return (check_contents(post) or check_time(post, time_after) or
            check_title(post) or check_source(post))