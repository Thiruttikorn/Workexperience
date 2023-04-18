//Part 2 Export and Import Function
// ------------------------ Export --------------------------------
// Higher-Order
export function circleLine(num){ 
    return num*6.28
    }
    function circleArea(num){ 
        return num*num*3.14
    }
    function circle(num,cfunction){ 
      return cfunction(num)
    }
export let line = circle(5,circleLine)
export let area = circle(5,circleArea)
    console.log("Circle : line : "+line+" Area : "+area)
    
    // Closure
      //1.
export function totalPrice(a) { 
       let price = 0; 
        return function(b){ 
            return function(c){ 
                return function(d){ 
                    return a+b+c+d+price;
    
                }
            }
        }
    } 
    console.log('total price is',totalPrice(35)(45)(69)(25),'baht'); 
    // 2.
export  const countStudent = (() =>{ 
        var count = 0 ;
        console.log('start to count :',count); 
        return () => {count +=1; console.log(count)}  
                                                     
    })();
    countStudent(); //1 
    countStudent(); //2
    countStudent(); //3
    
    //Default Parameter
export  let food = function(purchaser = 'unknown' ,foodname ='hamburger',price = 100){ 
        return 'Purchaser is: '+ purchaser +' ,Your order : ' + foodname + ' ,Price : ' + price +' baht' 
    
    }
    console.log(food()); 
    
    //4 Rest Parameter  
export function netflixCheck(a,b,...movies) { 
        console.log(a,b); 
        console.log(movies); 
        console.log(movies.length); 
     
      }
      netflixCheck('Friend Zone','Alive','Jurassic World','twilight');
    
// ------------------------ Import --------------------------------
//main.js
import {circleLine,line,area,totalPrice,
    countStudent,food,netflixCheck} 
    from './exporthw5.js'

//Function in Higher order 
console.log("Circle : line : "+line+" Area : "+area)

// Function in Closure
console.log('total price is',totalPrice(35)(45)(69)(25),'baht');
console.log('start to count :',count);
console.log(count)

// Function in Default parameter
console.log(a,b); 
console.log(movies); 
console.log(movies.length); 
netflixCheck('Friend Zone','Alive','Jurassic World','twilight');





