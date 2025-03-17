import json
import flet as ft

md1 = """
```
void main() {
  runApp(MaterialApp(
    home: Scaffold(
      body: ft.Markdown(data: markdownData),
    ),
  ));
}
```
"""
print(json.dumps(md1))



md1 = "\n```\nvoid main() {\n  runApp(MaterialApp(\n    home: Scaffold(\n      body: ft.Markdown(data: markdownData),\n    ),\n  ));\n}\n```\n"
md2 = """
```dart
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

void main() async {
  await setupDesktop();
  runApp(const FletApp(pageUrl: "http://localhost:8550"));
}
```
"""


def main(page: ft.Page):
    page.scroll = "auto"
    page.add(
        ft.Markdown(
            md1,
            selectable=True,
        )
    )
    page.add(
        ft.Markdown(
            md2,
            selectable=True,
            code_theme="atom-one-dark",
        )
    )

ft.app(main)





