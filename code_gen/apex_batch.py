from jinja2 import Environment, FileSystemLoader, Template
from datetime import datetime


class BatchClassTemplate:
    env = Environment(
        loader=FileSystemLoader('code_gen/templates/apexClasses'),

    )
    print(env.list_templates())
    batch_class_template = env.get_template(name='batch_template.cls')
    batch_class_test_template = env.get_template(name='batch_template_test.cls')

    def __init__(self):
        pass

    @classmethod
    def render_batch_class(cls, *args, make_test_class=True, **kwargs):
        """

        :param args:
        :param make_test_class:
        :param kwargs:
        :return:
        """
        render_vars = dict(*args, **kwargs)
        print(render_vars)
        render_vars['date'] = datetime.now()
        render_vars['batch_object_list'] = render_vars['batch_object'].lower() + '_list'

        if make_test_class:
            return cls.batch_class_template.render(render_vars), cls.batch_class_test_template.render(render_vars)

        else:
            return cls.batch_class_template.render(render_vars), None


