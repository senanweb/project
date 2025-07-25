import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.light(useMaterial3: true),
      home: MyProject(), //name your project
    );
  }
}
// your project
class MyProject extends StatelessWidget {
  const MyProject({super.key});
//start project
  @override
  Widget build(BuildContext context) {
    //body
    return  Scaffold
    (
      // Bar
      appBar: AppBar(
                      elevation: 15,
                      title: Text("MyApp"),
                      centerTitle: true,
                      leading: IconButton(onPressed: (){}, icon: Icon(Icons.menu, size:35,)),
                      actions: [
                               
                               IconButton(onPressed: (){}, icon: Icon(Icons.message, size:35,)),
                               IconButton(onPressed: (){}, icon: Icon(Icons.search, size:30,)),

                               ],
                    ),
      // body
      body: 
            Center(
              child: 
                    Text(
                          "Welcome To My Project 👋", 
                          style: TextStyle(fontSize: 27),
                        )
                  ),
    );
  }
}