import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:App_for_our_IA_tool/pages/search_page.dart';

import 'dart:convert';

import 'package:http/http.dart' as http;

class BookList extends StatefulWidget {
  @override
  _BookListState createState() => _BookListState();
}

class _BookListState extends State<BookList> {
  List<dynamic> bookList = [];

  void getBooks() async {
    String url = '127.0.0.1:8000';
    // final uri = Uri.parse(url);
    // print(uri);
    http.Response response = await http.get(Uri.http(url, '/api/books/'));
    String val = response.body;
    List<dynamic> data = jsonDecode(val);
    print("---------++++++++++++++++++$data");
    setState(() {
      data.forEach((value) {
        bookList.add(value);
        print(bookList);
      });
    });
  }

  @override
  void initState() {
    // TODO: implement initState
    getBooks();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Django BOOKLIST"),
        centerTitle: true,
      ),
      body: ListView(
        children: <Widget>[
          ListView.builder(
            shrinkWrap: true,
            itemCount: bookList.length,
            itemBuilder: (BuildContext context, int index) {
              return buildResultCard(bookList[index]);
            },
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.push(context,
                  MaterialPageRoute(builder: (context) => SearchPage()));
            },
            child: Text("Search Books"),
          ),
        ],
      ),
    );
  }
}

Widget buildResultCard(data) {
  return Padding(
    padding: const EdgeInsets.all(8.0),
    child: Column(
      children: <Widget>[
        ListTile(
          title: Text(data['name']),
          subtitle: Text("Rs.${data['price']}"),
        ),
        Divider(color: Colors.black)
      ],
    ),
  );
}
