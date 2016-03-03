import sublime, sublime_plugin, os, time

gsettings = {}

def plugin_loaded():
    global gsettings
    gsettings = sublime.load_settings("EasySyntax.sublime-settings")

class EasySyntax(sublime_plugin.EventListener):

    def on_load_async(self, view):

        psettings = sublime.active_window().project_data().get("EasySyntax")

        if not psettings:
            return

        psettings = psettings.get("map")

        if not psettings:
            return

        settings = gsettings.get("map", {})
        settings.update(psettings)

        print(settings)

        if view.settings().get("easy_syntax_applied"):
            return

        filename = view.file_name()

        if not filename:
            return

        ext = os.path.splitext(filename)[1].lstrip('.')
        # print("extension", ext)
        for syntax in settings:
            if ext in settings[syntax]:
                # print("Applying", syntax)
                view.settings().set("easy_syntax_applied", True)
                view.set_syntax_file(syntax)
                break



