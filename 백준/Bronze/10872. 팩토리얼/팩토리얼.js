let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

function inp(n) {
    let i =1
    let sum = 1;
         for(i; i < n; i++){
             sum += sum * i;
         }
         console.log(sum);

}

function ut(){
    let a = parseInt(input);
    if(a === 0){
        console.log(1);
    }
    else{
        inp(a);
    }
}
ut();

