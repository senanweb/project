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
      home: Project3(),
    );
  }
}
class Project3  extends StatelessWidget
{
  const Project3({super.key});
  @override
  Widget build(BuildContext context)
  {
    return  Scaffold 
    (
      appBar: AppBar
                    (
                      backgroundColor: const Color(0xBA5A42E4), // make background color
                      centerTitle: true,
                      title: Text("My Project"), 
                      leading: IconButton(onPressed: (){}, icon: Icon(Icons.menu, size: 35,)),
                      actions: 
                      [
                        IconButton(onPressed: (){}, icon: Icon(Icons.message, size: 35,)),
                        IconButton(onPressed: (){}, icon: Icon(Icons.search, size: 35,)),
                      ],                   
                    ),
    body: Center(
                  child: 
                        Text(
                              "Welcome To My Project", 
                              style: TextStyle(fontSize: 33) ,
                            ) ,
                ),
    );
  }
}