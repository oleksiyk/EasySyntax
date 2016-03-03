import sublime, sublime_plugin, os, time, re

gsettings = {}

def plugin_loaded():
    global gsettings
    gsettings = sublime.load_settings("EasySyntax.sublime-settings")

class EasySyntax(sublime_plugin.EventListener):
    def on_load(self, view):
        self.set_syntax(view)

    def set_syntax(self, view):
        if view.settings().get("easy_syntax_applied"):
            return

        view.settings().set("easy_syntax_applied", True)

        psettings = sublime.active_window().project_data().get("EasySyntax", {}).get("map", {})
        settings = gsettings.get("map", {})
        settings.update(psettings)

        # print(settings)

        filename = view.file_name()

        ext = os.path.splitext(filename)[1].lstrip('.')
        # print("extension", ext)
        for syntax in settings:
            if ext in settings[syntax].get("extensions", []):
                return self.apply_syntax(syntax, view)
            for pattern in settings[syntax].get("patterns", []):
                if re.search(pattern, filename):
                    return self.apply_syntax(syntax, view)

    def apply_syntax(self, syntax, view):
        # print("Applying", syntax)
        try:
            sublime.load_resource(syntax)
        except Exception:
            print("Syntax file not found", syntax)
        view.set_syntax_file(syntax)



