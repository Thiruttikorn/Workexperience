//ForEach() , shift() , unshift()
//foreach
//1.
var array1 = ['a', 'b', 'c']; 
console.log('The answer in forEach No.1:')
array1.forEach(element => console.log(element)); //เรียกข้อมูลในarrayมาแสดง
                    // a
                    // b
                    // c
//2.
console.log('The answer in forEach No.2 :');
let sum = 0; //ให้ค่าตั้งต้นของ sum เป็น 0
const numbers = [22,129,111,139,149]; //ข้อมูลที่มีอยู่ใน array
numbers.forEach(myFuction) //ใเรียกใช้parameter ชื่อ myFuction
function myFuction(item){ //มีparameterที่รับค่าไว้(item)
    sum += item; //ทำการลูปเอาค่าที่อยู่ในsum มาบวกเพิ่มไปเรื่อยๆจนหมดใน array
}
console.log(sum);

//3.
console.log('The answer in forEach No.3 :');
let devices = ['laptop','television','telephone','computer','headphones','microphone'];
devices.forEach(list); //ใช้forEachเรียกแสดงข้อมูลใน array มีlist เป็น parameter

function list(device, index){ //parameterไว้รับค่าในelement ของarrayนี้ว่าจะแสดงส่วนไหนบ้าง ในที่นี้จะรับและแสดงแค่ ตำแหน่งและitemที่มีอยู่
    if (device ==='computer'){ //ให้งื่อนไขไว้ว่าถ้าเป็นคำว่าcomputer 
        device = device.toUpperCase(); //ให้แสดงเป็นตัวพิมพ์ใหญ่
    }
    console.log(index,device); //เรียกดูแค่ตำแหน่งของข้อมูลและข้อมูลเท่านั้น
}

//shift()
//1.
console.log('The answer in shift No.1 :');
var a1 = [2,3,4,5,6,7];
a1.shift();          // shift จะตัดตัวเเรกใน array ออก 
                    //a1 = [ 3, 4, 5, 6, 7 ]
console.log(a1);
//2.
console.log('The answer in shift No.2 :');
var bakery = ['cake','bread','cookies','muffins','doughnuts'];
bakery.shift(); //ตัดคำว่า cake ออกไป เพราะมันคือตัวเริ่มต้นนั้นเอง
console.log(bakery);
//3.
console.log('The answer in shift No.3 :');
let beverages = ['coke','juice','tea','smoonthies'];
beverages.shift(); //ตัด coke ทิ้งไป
console.log(beverages);
//4.
console.log("--------------------------");
const array4 = [[4,5,6],7,8];
const array5 = [{id:9,name:"john"},10,11];
const array6 = [];

array4Shift  = array4.shift();
array5Shift  = array5.shift();
array6Shift  = array6.shift();

console.log(array4);
// output: Array [7,8]
console.log(array4Shift);
// output: Array [4,5,6]
console.log("--------------------------");
console.log(array5);
// output: Array [10,11]
console.log(array5Shift);
// output: Object {id:9,name:"john"}
console.log("--------------------------");
console.log(array6);
// output: Array []
console.log(array6Shift);
// output: Undefined
console.log("--------------------------");

//unshift()
//1.
console.log('The answer in unshift No.1 :');
var a2 = [1,3,4,5,6];
a2.unshift(7);       //unshift จะเป็นคำสั่งที่จะเติมตัวเลขที่กำหนด ใส่ไปข้างหน้าสุดของ array ชุดนั้น
                     //a2 = [ 7, 1, 3, 4, 5, 6 ]
//2.
a2.unshift(3,3,3,3) ;//สามารถที่จะเติมได้หลาย element
                    //a2 = [3,3,3,3,7,1,3,4,5,6]
console.log(a2);


//3,
console.log('The answer in unshift No.3 :');
const animals = ['cow','hippo','tiger','fish'];
animals.unshift('lion'); //add 'lion' 
console.log(animals);



