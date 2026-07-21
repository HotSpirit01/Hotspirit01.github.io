var money = 0;
var diff = 1;
var upgr = 0;
var upgrdf = 0;
var priseu = 100;
var prisep = 200;
var passd = 0;
var dox = 0;
var time = 5000;
var priset = 300;
var timed = 0;
const button = document.getElementById('button');
const pl = "Click +";
const dollar = "$"
const up = "Upgrade clicks costs ";
const pa = "passive income costs ";
const ti = "-time costs "
document.getElementById('click').textContent = pl + diff + dollar;
document.getElementById('clku').textContent = up + priseu + dollar;
document.getElementById('pass').textContent = pa + prisep + dollar;
document.getElementById('timeupg').textContent = ti + (priset+timed) + dollar;
setInterval(akca, 1);
function akca() {
if(money > 1000000){
    document.getElementById('money').innerHTML = "Money: " + (money/1000000).toFixed(1) + "M$"
}
}
function count() {
    console.log("money = " + money);
    money = money + diff;
    document.getElementById('money').innerHTML = "Money: " + money + "$";
}
function clku() {
    if(money < (priseu + upgrdf)) {
        error.textColor = 'red';
        error.textContent = "Not Enough money";
    }
    else {
        priseu = priseu + upgrdf;
        money = money - priseu;
        upgrdf = priseu;
        diff = 0.1*priseu;
        document.getElementById('upgaud').play();
        document.getElementById('money').innerHTML = "Money: " + money + "$";
        document.getElementById('click').textContent = pl + diff;
        document.getElementById('clku').textContent = up + (priseu+upgrdf) + dollar;
    }
}

function pass() {
    if(money < (prisep + passd)) {
        error.textColor = 'red';
        error.textContent = "Not Enough money";
    }
    else {
        prisep = prisep + passd;
        money = money - prisep;
        passd = prisep;
        dox = prisep*0.05;
        setInterval(plus, time);
        function plus() {
            money = money + dox;
            document.getElementById('money').innerHTML = "Money: " + money + "$";
            document.getElementById('passaud').play();
        }
        document.getElementById('money').innerHTML = "Money: " + money + "$";
        document.getElementById('pass').textContent = pa + (prisep+passd) + dollar;
        document.getElementById('clku').textContent = up + (priseu+upgrdf) + dollar;
    }
}
function minust() {
    if(money < (priset + timed)) {
        error.textColor = 'red';
        error.textContent = "Not Enough money";
    }
    else {
        priset = priset + timed;
        money = money - priset;
        timed = priset;
        time = 0.75*time;
        document.getElementById('passaud').play();
        document.getElementById('money').innerHTML = "Money: " + money + "$";
        document.getElementById('timeupg').textContent = ti + (priset+timed) + dollar;
    }
}
