// 防呆signup的name/username/password沒有輸入值
document.addEventListener("DOMContentLoaded", function(event) {
  let submitBtn=document.querySelector("#signup");
  let inputInfo = document.querySelectorAll(".input_signup");
  if(submitBtn){
    submitBtn.addEventListener('submit',function(event){
      for(let i=0;i<inputInfo.length;i++){
        if (!inputInfo[i].value){ 
          event.preventDefault();
          alert("請輸入註冊資料");
          break;
        }
      }
    });
  }
});

// 防呆signin的username/password沒有輸入值
document.addEventListener("DOMContentLoaded", function(event){
  let submitBtn=document.querySelector("#signin");
  let inputInfo = document.querySelectorAll(".input_signin");
  if(submitBtn){
    submitBtn.addEventListener("submit",function(event){
      for(let i=0;i<inputInfo.length;i++){
        if(!inputInfo[i].value){
          event.preventDefault();
          alert("請輸入帳號密碼");
          break;
        }
      }
    });
  }
});

//task6
let clickBtn=document.querySelectorAll(".deleteBtn");
let meg_id=document.querySelectorAll(".meg_id");
  for(let i =0;i<clickBtn.length;i++){
    if(clickBtn[i]){
      clickBtn[i].addEventListener("click",function(event){
        deleteMeg(meg_id[i].innerText);
      });
    }
  }

function deleteMeg(megID){
  var confirmation =confirm("確定要刪除嗎?");
  if(confirmation){
    var url="/deleteMessage";
    fetch(url,{
      method:'POST',
      headers:{ 'Content-Type':'application/json'},
      body: JSON.stringify({meg_id:megID})
    })
      .then(response=>response)
      .then(data=>{
        location.href="/member"; 
      })
      .catch(error=>console.error("Error:",error));
  }
}