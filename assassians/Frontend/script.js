const deviceList = document.querySelector('.device-list');

const FakeData = [
    {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }, {
        name: 'Device'
    }
]
FakeData.forEach((device, idx) => {
    deviceList.innerHTML += `<li>${device.name + " " + idx}</li>`
});