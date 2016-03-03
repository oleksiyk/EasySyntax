Add `"EasySyntax"` section to your `.sublime-project` file:

```JSON
{
    "EasySyntax": {
        "map": {
            "Packages/Javascript ES6/Javascript ES6.sublime-syntax": {
                "extensions": ["js"],

            },
            "Packages/Generic Config/GenericConfig.tmLanguage": {
                "extensions": ["conf", "cnf"],
                "patterns": ["conf\\.d/.+$"]
            },
            "Packages/YAML/YAML.sublime-syntax": {
                "patterns": ["ansible/(inventory|group_vars)/.*$", "Vagrantfile"]
            }
        }
    }
}
```

The above example will set `Javascript ES6` syntax for all files with `.js` extension in this project only.
