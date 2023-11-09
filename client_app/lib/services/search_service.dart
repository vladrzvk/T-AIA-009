import 'package:http/http.dart' as http;

class SearchService {
  static Future<String> searchDjangoApi(String query) async {
    // String url = 'http://192.168.212.1:8000/api/books/?search=$query';R

    String url = 'http://127.0.0.1:8000/api/books/?search=${query}';
    String host = '127.0.0.1:8000';
    String apiPath = 'api/books/';

    print('--------------------------$query');
    // Uri uri = Uri.parse(url);
    http.Response response =
        await http.get(Uri.http(host, apiPath, {'search': query}), headers: {
      "Access-Control-Allow-Origin": "*",
      'Content-Type': 'application/json',
      'Accept': '*/*'
    });
    return response.body;
  }
}
