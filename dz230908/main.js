
var result = [];
for(let i=0; i<10;i++){
    result.push(randomarray(-100,100));
}
//поиск максимума
let r = result[0];
for(let i=0; i<10;i++){
    if(result[i]>r){
        r = result[i];
    }
}

function randomarray(min,max){
    var rand = min-0.5 + Math.random() *(max-min+1);
    rand = Math.round(rand);
    return rand;
}
var p;
var t;
p = document.getElementById('out');
document.writeln(r);
p.innerHTML =  result;


