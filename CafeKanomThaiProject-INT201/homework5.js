// Higher order Function
function circleLine(num){ //คำนวณเส้นรอบวง เมื่อ num คือรัศมี
return num*6.28
}
function circleArea(num){ //คำนวณพื้นที่ เมื่อ num คือเส้นรัศมี
    return num*num*3.14
}
function circle(num,cfunction){ //ใช้งานสอง function ด้านบน
  return cfunction(num)
}
let line = circle(5,circleLine)
let area = circle(5,circleArea)
console.log("Circle : line : "+line+" Area : "+area)

// Closure
//1.
function outer() {
    let a = 10
    function inner() { //function นี้อยู่ภายใต้ functionข้างบน(outer)
      console.log('Number in Outer is :',a) //เรียกใช้ variableของfunctionภายนอก(outer)
    }
  
    return inner
  }
  
  const helloInner = outer() // สร้างvariableที่ returnออกมาจากfunction ที่ชื่อouter
  helloInner() // 10
//Closure
  //1.
function totalPrice(a) { //function เอาไว้เก็บค่า price 
    let price = 0; 
    return function(b){ //เป็นฟังก์ชันที่รับค่า b ที่ใส่มา แล้วreturn ออกไป
        return function(c){ //เป็นฟังก์ชันที่รับค่า c ที่ใส่มา แล้วreturn ออกไป
            return function(d){ ////เป็นฟังก์ชันที่รับค่า d ที่ใส่มา แล้วreturn ค่ารวมของparameterที่ดึงมาจากข้างนอกออกไป
                return a+b+c+d+price;

            }
        }
    }
} 
console.log('Answer of Closure No.1 :');
console.log('total price is',totalPrice(35)(45)(69)(25),'baht'); //ใส่ค่าลงไปตามลำดับ a(totlePrice),b,c,d,e(price ค่าเริ่มต้น=0) >>174
// 2.
console.log('Answer of Closure No.2 :');
const countStudent = (() =>{ //ประกาศfunction 
    var count = 0 ;
    console.log('start to count :',count); //บอกว่าเริ่มนับจาก 0
    return () => {count +=1; console.log(count)} //เรียกใช้ count ที่อยู่ข้างบนมาใช้งาน โดยจะทำการลูปเอาค่าที่อยู่ในcount 
                                                 //มาบวกเพิ่มไปเรื่อยๆทุกครั้งที่มีการนับหรือเรียกใช้countStudent
})();
countStudent(); //1 
countStudent(); //2
countStudent(); //3

//Default Parameter
let food = function(purchaser = 'unknown' ,foodname ='hamburger',price = 100){ //กำหนดค่าลงไป
    return 'Purchaser is: '+ purchaser +' ,Your order : ' + foodname + ' ,Price : ' + price +' baht' //return ค่าที่จะแสดงออกมา

}
console.log(food()); //เมื่อไม่มีการใส่ค่าใดๆเข้ามา จะไปเรียกdefault parameter มาแสดง
//console.log(food('Bobby')); //ถ้าใส่ค่าลงไปจะแสดงค่าที่ใส่นั้นลงไปนั้นมาแสดง

//4 Rest Parameter  
function netflixCheck(a,b,...movies) { //ฟังก์ชันที่มีrest parameter มาช่วยรองรับการเพิ่มเข้ามาของข้อมูล
    console.log(a,b); //แสดงข้อมูลที่มีกำหนดไว้ตั้งแต่แรก 2ตัวแรก
    console.log(movies); //แสดงข้อมูลที่เพิ่มเข้ามา โดยใช้rest parameterรับ
    console.log(movies.length); //แสดงlenght ที่movies นั้นรับข้อมูลเข้ามา
 
  }
  netflixCheck('Friend Zone','Alive','Jurassic World','twilight');
  
