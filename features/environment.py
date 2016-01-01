DEBUG = False


def before_all(context):
    global DEBUG
    DEBUG = context.config.userdata.getbool('DEBUG')


def after_step(context, step):
    if DEBUG and step.status == 'failed':
        import pdb
        pdb.post_mortem(step.exc_traceback)
