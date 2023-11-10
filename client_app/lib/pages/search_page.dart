import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:App_for_our_IA_tool/pages/book_list.dart';
import 'package:http/http.dart';
import '../services/search_service.dart';

class SearchPage extends StatefulWidget {
  @override
  _SearchPageState createState() => _SearchPageState();
}

class _SearchPageState extends State<SearchPage> {
  List<dynamic> searchResults = [];

  String search = "";

  // searchDjango(value) async {
  //   await SearchService.searchDjangoApi(value).then((responseBody) {
  //     String val = responseBody;

  //     List<dynamic> data = jsonDecode(val);
  //     print(val);

  //     setState(() {
  //       data.forEach((value) {
  //         searchResults.add(value);
  //         print(value);
  //       });
  //     });
  //   });

  void getBook(String search) async {
    String url = '127.0.0.1:8000';

    Response response =
        await get(Uri.http(url, '/api/books/', {"search": search}));
    String val = response.body;
    List<dynamic> data = jsonDecode(val);
    print("---------++++++++++++++++++$data");
    setState(() {
      data.forEach((value) {
        searchResults.add(value);
        print(searchResults);
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text("Django API Search"),
          centerTitle: true,
        ),
        body: ListView(
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.all(10.0),
              child: TextField(
                onChanged: (val) {
                  searchResults.clear();
                  // searchDjango(val);
                  search = val;
                },
                decoration: InputDecoration(
                  contentPadding: EdgeInsets.only(left: 25.0),
                  hintText: 'Search Book',
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(4.0),
                  ),
                  suffixIcon: IconButton(
                    icon: Icon(Icons.search),
                    onPressed: () async {
                      getBook(search);
                    },
                  ),
                ),
              ),
            ),
            SizedBox(
              height: 10.0,
            ),
            ListView.builder(
              shrinkWrap: true,
              itemCount: searchResults.length,
              itemBuilder: (BuildContext context, int index) {
                return buildResultCard(searchResults[index]);
              },
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => BookList()));
              },
              child: Text("SEE ALL BOOKS"),
            ),
          ],
        ),
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
