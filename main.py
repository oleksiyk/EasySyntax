import sublime, sublime_plugin, os, time

gsettings = {}

def plugin_loaded():
    global gsettings
    gsettings = sublime.load_settings("EasySyntax.sublime-settings")

class EasySyntax(sublime_plugin.EventListener):
    def on_load_async(self, view):
        self.set_syntax(view)

    def set_syntax(self, view):
        if view.settings().get("easy_syntax_applied"):
            return

        view.settings().set("easy_syntax_applied", True)

        psettings = sublime.active_window().project_data().get("EasySyntax")

        if not psettings:
            return

        psettings = psettings.get("map")

        if not psettings:
            return

        settings = gsettings.get("map", {})
        settings.update(psettings)

        # print(settings)

        filename = view.file_name()

        if not filename:
            return

        ext = os.path.splitext(filename)[1].lstrip('.')
        # print("extension", ext)
        for syntax in settings:
            if ext in settings[syntax]:
                # print("Applying", syntax)
                try:
                    sublime.load_resource(syntax)
                except Exception:
                    print("Syntax file not found", syntax)
                view.set_syntax_file(syntax)
                break



