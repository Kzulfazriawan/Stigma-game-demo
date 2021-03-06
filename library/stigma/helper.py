from os import path
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.animation import Animation


def classMaker(*args):

    if isinstance(args, tuple):
        return type('lamdaobject', args, {})


def clocker(function, schedule, duration = 0):
    clo_thread = Clock

    if schedule == 'once':
        if duration > 0 and (isinstance(duration, int) or isinstance(duration, float)):
            clo_thread.schedule_once(function, duration)
        else:
            clo_thread.schedule_once(function)

    elif schedule == 'trigger':
        clo_thread.schedule_trigger(function)

    return clo_thread


def animation(widget, animate):
    '''

    '''
    if widget is not None:
        if isinstance(animate, list) or isinstance(animate, tuple):

            animator = Animation()
            for v in animate:
                animator &= Animation(**v)

            animator.start(widget)


def logs(what='', message=''):
    if what == 'info':
        Logger.info(message)
    elif what == 'debug':
        Logger.debug(message)
    elif what == 'error':
        Logger.error(message)
    elif what == 'warning':
        Logger.warning(message)
        

def eventAttach(function=None, action='on_press'):
    '''
    eventAttach(unbound_object, str_action)

    create an method which ready to attach into event or bound, it will
    generate the method that has single parameter into event function.

    .. notes:
        is required to set the parameter into your function, even you no
        need it but it have to. and also set the widget with variable "params"
    '''

    if function is not None:
        if action == 'on_press':
            event = lambda instance : function(instance.params)
        elif action == 'on_touch_down':
            event = lambda instance, touch: function(instance.params)

        return event


def kivyBuilder(*args):
    '''
    this function is used to open builder language kivy.
    '''
    if args is not None:
        kivy_path = path.join(*args)

        if path.isfile(kivy_path):
            return Builder.load_file(kivy_path)