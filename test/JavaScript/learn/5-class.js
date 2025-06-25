// make class
class Person{
    constructor(name,work)
    {
        this.name = name;
        this.work = work;
    }
}
// make object for input
const myName = new Person("sinan",true);
// print
console.log(myName)


////////////////////////////////////
// EXAMPLE//
////////////////////////////////////




// CLASS
class Persons {
    constructor(name,work)
    {
        this.name = name;
        this.work = work;
    }
    myNames()
    {
        console.log("My name is" +" "+ this.name);
    }
}
///////////////////////////////////////////////////////
// OBJECT
var person ={
    name: "sinan",
    age:44,
    work:true,
    myNames:function()
    {
        console.log("My name is" + this.name);
    }
}
// print
console.log(person);

// new input for object
var myFunc = new Persons("Nadom",true);
myFunc.myNames();

