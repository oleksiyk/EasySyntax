import sublime, sublime_plugin, os, time

class EasySyntax(sublime_plugin.EventListener):

    def on_load_async(self, view):
        settings = sublime.active_window().project_data().get("EasySyntax");

        if not settings:
            return

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
                view.set_syntax_file(syntax + ".sublime-syntax")
                break



