import 'package:flutter/material.dart';
import 'package:App_for_our_IA_tool/pages/book_list.dart';
import 'pages/search_page.dart';

void main() {
  runApp(FlutterSearch());
}

class FlutterSearch extends StatefulWidget {
  @override
  _FlutterSearchState createState() => _FlutterSearchState();
}

class _FlutterSearchState extends State<FlutterSearch> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: BookList(),
    );
  }
}
