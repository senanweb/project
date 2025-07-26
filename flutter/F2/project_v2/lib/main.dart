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
      home: Project2(),
    );
  }
}


class Project2 extends StatelessWidget {
  const Project2({super.key});
  @override
  Widget build(BuildContext context) {
    return  Scaffold 
    (
      appBar: AppBar
                    (
                      backgroundColor: Colors.blue[300], // make background color
                      centerTitle: true,
                      title: Text("Project2"),
                      
                    ),
    );
    
  }
}
