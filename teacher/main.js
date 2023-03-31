function isClick(getInfo){
    var getClass=getInfo.getAttribute("class")
    var getID=getInfo.parentNode.id
    console.log(getClass,getID)
    var t={
        'From':'student',
        'to':'lib',
        'ID':getID,
        'need':'getAndChangeIDStstus',
        'info':[getClass]
    }
    client.publish("pingHandSystem/MQTT", JSON.stringify(t))
}
function allClick(getInfo){
    var getClass=getInfo.getAttribute("class")
    var t={
        'From':'control',
        'to':'lib',
        'ID':"01",
        'need':'allRelax',
        'info':[getClass]
    }
    client.publish("pingHandSystem/MQTT",JSON.stringify(t))
}

var client = mqtt.connect("ws://test.mosquitto.org:8080");

client.on('connect', ()=>{
    console.log('connected.');
    client.subscribe("pingHandSystem/MQTT")
    client.on("message", function (topic, payload) {
        getValue=JSON.parse(payload)
        if(getValue['need']=='sendStatus'){
            if(getValue['info'][0]){
                var heading = document.querySelectorAll(".hand")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "yellow";
                // document.getElementById(getValue['ID']).getElementsByClassName('hand').backgroundColor="yellow"
                // console.log(document.getElementById(getValue['ID']).getElementsByClassName('hand'))
            }else{
                // document.getElementById("hand").style.backgroundColor="gray"
                var heading = document.querySelectorAll(".hand")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "gray";
            }
            if(getValue['info'][1]){
                var heading = document.querySelectorAll(".A")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "yellow";
                // document.getElementById(getValue['ID']).getElementsByClassName('hand').backgroundColor="yellow"
                // console.log(document.getElementById(getValue['ID']).getElementsByClassName('hand'))
            }else{
                // document.getElementById("hand").style.backgroundColor="gray"
                var heading = document.querySelectorAll(".A")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "gray";
            }
            if(getValue['info'][2]){
                var heading = document.querySelectorAll(".B")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "yellow";
                // document.getElementById(getValue['ID']).getElementsByClassName('hand').backgroundColor="yellow"
                // console.log(document.getElementById(getValue['ID']).getElementsByClassName('hand'))
            }else{
                // document.getElementById("hand").style.backgroundColor="gray"
                var heading = document.querySelectorAll(".B")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "gray";
            }
        }
        if(getValue['need']=='returnReset'){
            console.log(getValue)
            if(getValue['info'][2]){
                var heading = document.querySelectorAll(".hand")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "yellow";
                // document.getElementById(getValue['ID']).getElementsByClassName('hand').backgroundColor="yellow"
                // console.log(document.getElementById(getValue['ID']).getElementsByClassName('hand'))
            }else{
                // document.getElementById("hand").style.backgroundColor="gray"
                var heading = document.querySelectorAll(".hand")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "gray";
            }
            if(getValue['info'][3]){
                var heading = document.querySelectorAll(".A")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "yellow";
                // document.getElementById(getValue['ID']).getElementsByClassName('hand').backgroundColor="yellow"
                // console.log(document.getElementById(getValue['ID']).getElementsByClassName('hand'))
            }else{
                // document.getElementById("hand").style.backgroundColor="gray"
                var heading = document.querySelectorAll(".A")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "gray";
            }
            if(getValue['info'][4]){
                var heading = document.querySelectorAll(".B")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "yellow";
                // document.getElementById(getValue['ID']).getElementsByClassName('hand').backgroundColor="yellow"
                // console.log(document.getElementById(getValue['ID']).getElementsByClassName('hand'))
            }else{
                // document.getElementById("hand").style.backgroundColor="gray"
                var heading = document.querySelectorAll(".B")
                var headingchange=heading[parseInt(getValue['ID'])-1]
			    headingchange.style.backgroundColor = "gray";
            }
            var paras = document.querySelectorAll(".name"); // 选中所有 class 为 my-para 的元素
            for(var i = 0; i < paras.length; i++) {
                var para = paras[i];
                console.log("sdsafdsfadsfasd")
                console.log(String(getValue["ID"]))
                console.log(String(para.parentNode.id))
                if(String(para.parentNode.id) === String(getValue["ID"])) { // 判断是否为目标元素
                    console.log("in")
                    para.textContent = getValue['info'][1];
                }
            }
        }
    });
    // client.publish("mee", "hello");
});