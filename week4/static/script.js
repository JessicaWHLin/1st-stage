document.addEventListener("DOMContentLoaded", function(event) {
  let submitButton=document.querySelector("#result");
  let checkBox=document.querySelector(".checkbox");
  if(submitButton){
    submitButton.addEventListener('submit',function(event){
        if (!checkBox.checked){
          event.preventDefault();
          alert("Please check the checkbox first.");
        }
      });
    }
});

// task4
// 判斷正整數
function isPositiveInteger(data){
  if(parseFloat(data) %1 !== 0){return false;} 
  if(parseFloat(data) <= 0){return false;}
  return true;
}
document.addEventListener("DOMContentLoaded", function(event) {
let submitButton2=document.querySelector(".submitInt");
let checkInt=document.querySelector(".integer");
if(submitButton2){
submitButton2.addEventListener('click',function(event){
  if (isPositiveInteger(checkInt.value) !== true){
    event.preventDefault();
    alert("Please enter a positive number.");
  }
  else{ submitButton2.click=getInt();}
});
}
});

function getInt(){
  var inputInt=parseInt(document.querySelector(".integer").value); //parseInt():字串轉正整數
  var url = "/square/" + inputInt; //建立帶有動態參數的URL
  fetch(url)
    .then(response=>response)
    .then(data=>{
      location.href=url; //瀏覽器重新導向需求的URL
    })
    .catch(error=>console.error("Error:", error));
}