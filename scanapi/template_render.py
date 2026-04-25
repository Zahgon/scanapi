import curlify2
from jinja2 import Environment, FileSystemLoader, PackageLoader


def render(template_path, context, is_external=False):
    """Controller function that handles the Jinja2 rending of the template."""
    pass


def _loader(is_external):
    """
    Private function that either returns Jinja2 FileSystemLoader or the
    PackageLoader.
    """
    pass


def render_body(request):
    """Render body according to its request content type."""
    pass
