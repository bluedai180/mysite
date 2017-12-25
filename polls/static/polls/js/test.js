/**
 * Created by HIPADUSER on 2017/12/25.
 */

var user = document.getElementById("user");
var pwd = document.getElementById("pwd");
var a = document.getElementById("a");
var b = document.getElementById("b");
var result = document.getElementById("result");

function test() {
    console.log("user = " + user.value);
    console.log("pwd = " + pwd.value);
}

function sum_test() {
    $.get("/polls/add/", {'a': a.value, 'b': b.value}, function (ret) {
        result.innerHTML = ret;
    })
}
