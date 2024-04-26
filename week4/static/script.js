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


