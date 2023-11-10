import 'dart:convert';

import 'package:http/http.dart';

class SearchService {
  // static Future<String> searchDjangoApi(String query) async {
  //   // String url = 'http://192.168.212.1:8000/api/books/?search=$query';

  //   String url = 'http://127.0.0.1:8000/api/books/?search=$query';
  //   String host = '127.0.0.1:8000';
  //   String apiPath = 'api/books/';

  //   // Uri uri = Uri.parse(url);
  //   print(await get(Uri.http(host, apiPath, {'search': query}),
  //       headers: {"Access-Control-Allow-Origin": "*", 'Accept': '*/*'}));
  //   print('ok');
  //   Response response = await get(
  //       Uri.http(host, apiPath, {'search': query.toString()}),
  //       headers: {"Access-Control-Allow-Origin": "*", 'Accept': '*/*'});

  //   print(response.body.toString());
  //   return response.body.toString();
  // }
}
