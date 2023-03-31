function fRename(){
    console.log("被按了1");
    t={
        'From':'student',
        'to':'lib',
        'ID':document.getElementById("IDinput").value,
        'need':'rename',
        'info':[document.getElementById("nameInput").value]
    }
    client.publish("pingHandSystem/MQTT", JSON.stringify(t))
}
function fHang(){
    var t={
        'From':'student',
        'to':'lib',
        'ID':document.getElementById("IDinput").value,
        'need':'getAndChangeIDStstus',
        'info':['hand']
    }
    client.publish("pingHandSystem/MQTT", JSON.stringify(t))
}
function fA(){
    var t={
        'From':'student',
        'to':'lib',
        'ID':document.getElementById("IDinput").value,
        'need':'getAndChangeIDStstus',
        'info':['A']
    }
    client.publish("pingHandSystem/MQTT", JSON.stringify(t))

}
function fB(){
    var t={
        'From':'student',
        'to':'lib',
        'ID':document.getElementById("IDinput").value,
        'need':'getAndChangeIDStstus',
        'info':['B']
    }
    client.publish("pingHandSystem/MQTT", JSON.stringify(t))

}

var client = mqtt.connect("ws://test.mosquitto.org:8080");

client.on('connect', ()=>{
    console.log('connected.');
    client.subscribe("pingHandSystem/MQTT")
    client.on("message", function (topic, payload) {
        getValue=JSON.parse(payload)
        if(getValue['need']=='sendStatus'){
            if(getValue['info'][0]){
                document.getElementById("hand").style.backgroundColor="blue"
            }else{
                document.getElementById("hand").style.backgroundColor="#4CAF50"
            }
            if(getValue['info'][1]){
                document.getElementById("A").style.backgroundColor="blue"
            }else{
                document.getElementById("A").style.backgroundColor="#4CAF50"
            }
            if(getValue['info'][2]){
                document.getElementById("B").style.backgroundColor="blue"
            }else{
                document.getElementById("B").style.backgroundColor="#4CAF50"
            }
        }
    });
    // client.publish("mee", "hello");
});