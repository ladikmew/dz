
var fname1 = ["Друг ёжик","Друг белочка","<3"];
var fname2 = ["Друг кролик","Друг енотик", "<3"];
var itog = []
let k = -1;


function g(el){
    function f(){
            k = k+1;
            document.getElementById("maincard").innerHTML = el.getElementsByClassName("pic")[k].innerHTML;
            var t = el.getElementsByClassName("pic")
            itog.push(t[k].id);
            const mybutton1 = document.getElementById("btn2");
            mybutton1.innerHTML = fname2[k];
            const mybutton = document.getElementById("btn1");
            mybutton.innerHTML = fname1[k];
            console.log(k);
            console.log(itog);
    };
    return f;
}


function main(){
    let y = document.getElementsByClassName('rat');
    for(let i=0; i < y.length; i++){
        y[i].onclick = g(y[i]);
    };
    let x = document.getElementsByClassName('raty');
    for(let i=0; i < x.length; i++){
        // console.log("#")
        x[i].onclick = kop(x[i]);
    };
}

function kop(ell){
    function h(){
        
        console.log(itog);
        if (itog[0] == 1 && itog[1] == 3 && itog[2] == 5){
            document.getElementById("maincard").innerHTML = ell.getElementsByClassName("lastpic")[0].innerHTML;
        }
        if (itog[0] == 1 && itog[1] == 4 && itog[2] == 5){
            document.getElementById("maincard").innerHTML = ell.getElementsByClassName("lastpic")[1].innerHTML;
        }
        if (itog[0] == 1 && itog[1] == 3 && itog[2] == 6){
            document.getElementById("maincard").innerHTML = ell.getElementsByClassName("lastpic")[2].innerHTML;
        }
        if (itog[0] == 1 && itog[1] == 4 && itog[2] == 6){
            document.getElementById("maincard").innerHTML = ell.getElementsByClassName("lastpic")[3].innerHTML;
        }
        if (itog[0] == 2 && itog[1] == 3 && itog[2] == 5){
            document.getElementById("maincard").innerHTML = ell.getElementsByClassName("lastpic")[4].innerHTML;
        }
        if (itog[0] == 2 && itog[1] == 3 && itog[2] == 6){
            document.getElementById("maincard").innerHTML = ell.getElementsByClassName("lastpic")[5].innerHTML;
        }
        if (itog[0] == 2 && itog[1] == 4 && itog[2] == 5){
            document.getElementById("maincard").innerHTML = ell.getElementsByClassName("lastpic")[6].innerHTML;
        }
        if (itog[0] == 2 && itog[1] == 4 && itog[2] == 6){
            document.getElementById("maincard").innerHTML = ell.getElementsByClassName("lastpic")[7].innerHTML;
        }
    
    };
    return h;
}



document.addEventListener("DOMContentLoaded", main)
