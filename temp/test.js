// //只有一個物件時
// const obj={a:1,b:2,c:3};
// // objNew=[];
// for(let key in obj){
//         console.log("Key="+key,"Value="+obj[key]);
//         // objNew.push(obj[key]);
// }
//         // console.log(objNew);


// //有多個物件時
// const obj2=[{a:1,b:2,c:3},{a:1,b:2,c:3}];
// for(let i=0;i<obj2.length;i++){
        // for(let key in obj2[i]){
                // console.log("Key="+key,"Value="+obj2[i][key]);
        // }
        // console.log(obj2[i]);
        // }
// }

//         for(var i=0;i<3;i++){
//            console.log(i);
//         }
    
// console.log("i=",i);
// let a=[1,2,3];
// let b=[[{1:2,2:4}]];
// console.log(b[0][0]);
 var dataView = new DataView( new ArrayBuffer(8));
 dataView.setFloat64(0,3);
 var byteSize = dataView.byteLength;
 console.log("數字所佔的大小為 = ",byteSize);




