// 防呆signup的name/username/password沒有輸入值
document.addEventListener("DOMContentLoaded", function(event) {
  let submitBtn=document.querySelector("#signup");
  let inputInfo = document.querySelectorAll(".input_signup");
  let password_limit=document.querySelector("#inipassword");
  let result= document.querySelector("#signupResult");
  let re=/^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@#$%])[a-zA-Z\d@#$%]{4,8}$/;
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
    // 註冊帳號輸入限制:英文數字跟@#$%,4-8字內
    //取出註冊password的node→建立正規表達式建立判斷function→按鈕submit→正規表達式不符合(value=null)就跳出預警視窗
    submitBtn.addEventListener('submit',function(e){
      if(password_limit.value.match(re)==null){
        // console.log("username_limit.value.match(re)= "+username_limit.value.match(re));
        e.preventDefault();
        alert("請設定4~8碼含英文及數字及@#$%的密碼");
      }
      else{result.textContent="註冊成功";}
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

//刪除留言
let clickBtn=document.querySelectorAll(".deleteBtn");
let meg_id=document.querySelectorAll(".meg_id");
  for(let i =0;i<clickBtn.length;i++){
    if(clickBtn[i]){
      clickBtn[i].addEventListener("click",function(event){
        deleteMeg(meg_id[i].innerText);
      });
    }
  }
//查詢會員姓名
let queryBtn=document.querySelector(".queryBtn");
let queryUsername=document.querySelector("#queryUsername");
if(queryBtn){
  queryBtn.addEventListener("click",function(event){
    query_username(queryUsername.value);
  })
}
//更新會員姓名
let updateBtn=document.querySelector(".updateBtn");
let updateUsername=document.querySelector("#updateUsername");
if(updateBtn){
  updateBtn.addEventListener('click',function(event){
    update_username(updateUsername.value);
  })
}

function deleteMeg(megID){
  let confirmation =confirm("確定要刪除嗎?");
  if(confirmation){
    let url="/deleteMessage";
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

function query_username(input){
  let url="/api/member"+"?username="+input;
  fetch(url)
    .then(response=>response.json())
    .then(data=>{
      let showQueryResult=document.querySelector(".usernameResults");
      if(data != null){
        let name=data.data["name"];
        let username=(data.data["username"]);
        showQueryResult.textContent=name+" ( "+username+" ) ";
      }
      else{ 
        let noData="沒有資料";
        showQueryResult.textContent=noData;
      };
    })
    .catch(error=>console.log("Error:",error));   
}

function update_username(input){
  let url="/api/member";
  fetch(url,{
    method:'PATCH',
    headers:{ 'Content-Type':'application/json'},
    body:JSON.stringify({"name":input})
  })
  .then(response=>response.json())
  .then(data=>{
    let updateUsernameResult=document.querySelector(".updateResults");
    let current_name=document.querySelector("#current_name");
    let old_meg_name=document.querySelectorAll(".username");
    if(data.data["ok"] ==true){
      updateUsernameResult.textContent="更新成功";
      for(let i=0;i<old_meg_name.length;i++){
        if(old_meg_name[i].textContent===current_name.textContent){
          old_meg_name[i].textContent=input;
        }
      }
      current_name.textContent=input;
    }
    else{
      updateUsernameResult.textContent="更新失敗";
    };
  })
  .catch(error=>console.log("Error:",error));
}