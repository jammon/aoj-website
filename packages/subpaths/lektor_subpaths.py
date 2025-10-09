# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin


class SubpathsPlugin(Plugin):
    name = "Subpaths"
    description = "`is_subpath` checks if an url is a child of another url."

    def on_process_template_context(self, context, **extra):
        def is_subpath(child: str, parent: str):
            if child == parent:
                return True
            return parent != "/" and child.startswith(parent)

        context["is_subpath"] = is_subpath
