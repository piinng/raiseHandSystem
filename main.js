function renameOnclick(){
    console.log("被按了1");
};

var client = mqtt.connect("ws://test.mosquitto.org:8080");

client.on('connect', ()=>{
    console.log('connected.');
    client.subscribe("mee")
    client.on("message", function (topic, payload) {
        getValue=JSON.parse(payload)
    });
    // client.publish("mee", "hello");
});c    