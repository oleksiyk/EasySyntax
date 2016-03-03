Add `"EasySyntax"` section to your `.sublime-project` file:

```JSON
{
    "EasySyntax": {
        "map": {
            "Packages/Javascript ES6/Javascript ES6.sublime-syntax": ["js"],
            "Packages/Generic Config/GenericConfig.tmLanguage": ["conf", "cnf"]
        }
    }
}
```

The above example will set `Javascript ES6` syntax for all files with `.js` extension in this project only.
