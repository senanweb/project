
// make condition
var myTest = 10;   // var
if (myTest == 10){
    console.log("Nice");
}
else {console.log("Please Try Again")}


// ===========================
// make object
var cars = {
    price: 9,
    color:"blue",
    doors:2
}
// if-else
if (cars.price < 10 && cars.color === "blue")
    {
        console.log("woww, nice car")
    }
else if(cars.price < 10 && cars.color === "blue" || cars.doors === 4)
    {console.log("i will thing")}
else{console.log("i will back soon")}