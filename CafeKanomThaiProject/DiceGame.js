let rounds = 3 ; 
let player1 = { name : " Jotaro "}; 
let player2 = { name : " Dio "}; 

    function gameOn(){ 

     console.log("\n Game On \n");

    for(let i = 0; i < rounds ;i++){

      console.log(" Round : "+(i+1)+" G0!!!! \n");
      console.log(player1.name+" throw the dice")

      function player1ThrowsDice() {
      let dice = [1,2,3,4,5,6];
      let rd = Math.floor(Math.random()*dice.length);
      return dice[rd]; }

      player1.points = player1ThrowsDice();
     console.log(player1.name+" got "+player1.points+" points \n");
    
     console.log(player2.name+" throw the dice")

      function player2ThrowsDice() {
      let dice = [1,2,3,4,5,6];
      let rd = Math.floor(Math.random()*dice.length);
      return dice[rd]; }
      
     player2.points = player2ThrowsDice();
     console.log(player2.name+" got "+player2.points+" points \n");
     console.log("Result of this round \n");

     function resultOfRounds(){
       if(player1.points>player2.points){
         p1result = "Win"
         p2result = "Lose"
       }
       else if(player1.points<player2.points){
        p2result = "Win"
        p1result = "Lose"
      }
      else{
        p1result = "Draw"
        p2result = "Draw"
      }
      return {p1result,p2result}
    }
     let result = resultOfRounds();
     player1.result = result.p1result;
     player2.result = result.p2result;
     console.log(player1.name+" "+player1.result);
     console.log(player2.name+" "+player2.result+" \n");
    }
}
console.log(gameOn())
