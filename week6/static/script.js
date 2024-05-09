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
