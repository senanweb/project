import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.light(useMaterial3: true),
      home: M_project(),
    );
  }
}

class M_project extends StatelessWidget {
  const M_project({super.key});
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: const Color(0xBA5A42E4), // make background color
        centerTitle: true,
        title: Text("Show App"),
        leading: IconButton(onPressed: () {}, icon: Icon(Icons.menu, size: 35)),
        actions: [
          IconButton(onPressed: () {}, icon: Icon(Icons.message, size: 35)),
          IconButton(onPressed: () {}, icon: Icon(Icons.search, size: 35)),
        ],
      ),
      floatingActionButton: FloatingActionButton(
                                                  onPressed: () {},
                                                  child: Icon(Icons.add),
                                                ), //this is button +
    
      body: Center(
                    child:
                          Text(
                                "Welcome To My Page",
                                style: TextStyle(fontSize: 33, color: Colors.blue, decoration: TextDecoration.underline,fontWeight: FontWeight.bold) ,
                                maxLines: 2,
                                overflow: TextOverflow.ellipsis, //......
                                textAlign: TextAlign.left,
                                textDirection: TextDirection.ltr, // this is for arabic write
                                
                              ) ,
                  ),
    );
  }
}
